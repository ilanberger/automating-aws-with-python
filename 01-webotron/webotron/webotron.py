#!/user/bin/python
# -*- coding: utf-8 -*-


"""weboton:deploy website to aws.

webotron automates the process of deploying static web
- configure AWS S3 black
    -create then
    - set them up for static website hosting
    - deploy local files to them
-- configure DNS with with AWS S3
-configure a content delivery network and SSL with AWS routh53

"""


import boto3
# import sys
import click

from bucket import BucketManager

session = None
bucket_manager = None
# s3 = session.resource("s3")


@click.group()
@click.option('--profile',default=None,
    help="Use a given AWS profile.")
def cli(profile):
    """Webotron deploys websites to AWS."""
    global session, bucket_manager
    session_cfg = {}
    #session_cfg['profile_name'] = 'pythonAutomation'
    if (profile != None):
        print(1)
        session_cfg['profile_name'] = profile
    else:
        print(2)
        session_cfg['profile_name'] = 'pythonAutomation'
    print(session_cfg)
    session = boto3.Session(**session_cfg)
    # Session(profile_name="pythonAutomation")
    bucket_manager = BucketManager(session)


@cli.command("list-buckets")
def list_buckets():
    """List all s3 buckets."""
    for bucket in bucket_manager.all_buckets():
        print(bucket)


@cli.command("list-bucket-objects")
@click.argument("bucket")
def list_bucket_objects(bucket):
    """List objects in an s3 bucket."""
    for obj in bucket_manager.all_objects(bucket):
        print(obj)


@cli.command("setup-bucket")
@click.argument('bucket')
def setup_bucket(bucket):
    """Create and configure S3 bucket."""
    s3_bucket = bucket_manager.init_bucket(bucket)
    bucket_manager.set_policy(s3_bucket)
    bucket_manager.configure_website(s3_bucket)
    return


@cli.command("sync")
@click.argument("pathname", type=click.Path(exists=True))
@click.argument("bucket")
def sync(pathname, bucket):
    """Sync content of PATHNAME to BUCKET."""
    bucket_manager.sync(pathname, bucket)


if __name__ == "__main__":
    # print(sys.argv)
    # list_buckets()
    cli()
