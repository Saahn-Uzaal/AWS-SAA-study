resource "aws_s3_bucket" "my-example-s3-bucket" {

  tags = {
    Name        = "My bucket"
    Environment = "Dev"
  }
}