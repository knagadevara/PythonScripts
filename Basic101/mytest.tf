provider "aws" {
    access_key =    "${ASKMEID}"
    secret_key =    "${ASKMEPASS}"
    region =    "ap-south-1"  
}

resource "aws_s3_bucket" "my_s3_bucket" {
    bucket = "my_s3_bucket"
    region = "ap-south-1"
    
}