import boto3
import uuid

# AWS Region muốn tạo S3 bucket
region = "ap-southeast-1"

# Nhập tên từ bàn phím
name = input("Enter bucket name: ")

# Tạo tên bucket hoàn chỉnh
bucket_name = f"my-example-bucket-{name}"

# Tạo S3 client bằng boto3
# Client này sẽ dùng để gọi các API của Amazon S3
s3 = boto3.client(
    "s3",
    region_name=region
)

# Tạo S3 bucket
s3.create_bucket(
    Bucket=bucket_name,

    # Chỉ định Region nơi bucket được tạo
    CreateBucketConfiguration={
        "LocationConstraint": region
    }
)

# Thông báo sau khi tạo bucket thành công
print(f"Created bucket: {bucket_name}")
s3.put_object(
    Bucket=bucket_name,
    Key="example.txt",
    Body= open("example.txt", "r").read()
)