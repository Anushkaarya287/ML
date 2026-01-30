import boto3
import time
import json
from datetime import datetime

class CloudExtractor:
    def __init__(self, bucket_name, lock_prefix="locks/"):
        self.s3 = boto3.client('s3')
        self.bucket = bucket_name
        self.lock_prefix = lock_prefix
    
    def acquire_lock(self, process_id, timeout_minutes=30):
        """Create a lock file to prevent concurrent processing"""
        lock_key = f"{self.lock_prefix}{process_id}.lock"
        
        # Check 
        try:
            lock_info = self.s3.get_object(Bucket=self.bucket, Key=lock_key)
            lock_data = json.loads(lock_info['Body'].read())
            
            
            lock_time = datetime.fromisoformat(lock_data['timestamp'])
            if (datetime.now() - lock_time).seconds < timeout_minutes * 60:
                return False  
            
        except self.s3.exceptions.NoSuchKey:
            pass  
        lock_data = {
            'process_id': process_id,
            'timestamp': datetime.now().isoformat(),
            'host': 'your-hostname',
            'status': 'processing'
        }
        
        self.s3.put_object(
            Bucket=self.bucket,
            Key=lock_key,
            Body=json.dumps(lock_data)
        )
        return True
    
    def release_lock(self, process_id):
        """Remove lock file after processing"""
        lock_key = f"{self.lock_prefix}{process_id}.lock"
        self.s3.delete_object(Bucket=self.bucket, Key=lock_key)
    
    def extract_with_lock(self, process_id, data_prefix):
        """Safe extraction with lock mechanism"""
        if not self.acquire_lock(process_id):
            print(f"Process {process_id} is already running or lock exists")
            return
        
        try:
           
            json_data = self.collect_json_data(data_prefix)
            print(f"Collected {len(json_data)} JSON files")
            return json_data
        finally:
            self.release_lock(process_id)