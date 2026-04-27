import boto3

s3 = boto3.client('s3')

def upload_file():
    s3.upload_file('../sample_data/orders.csv', 'your-bucket-name', 'raw/orders.csv')

if __name__ == "__main__":
    upload_file()
