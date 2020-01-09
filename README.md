## TMNT Wikipedia Bot

Every 60 minutes this Python script posts to https://twitter.com/CamptownWiki

### Why

For fun! Inspired by https://twitter.com/wiki_tmnt

### How

When it runs, it:
- Pulls 10 random Wikipedia article titles
- Checks if they are in the correct meter
- Looks to see if another stored title rhymes with it
  - If not, pull 10 more articles ad infinitum until a match is found
- Post the verse to @CamptownWiki on Twitter

### Environment

For @CamptownWiki it runs in AWS Lambda with an S3 bucket for storage (should probably be DynamoDB).

### Configuration

Mostly in `lib/constants.py`, some is environment variables because Lambda likes those.

### TODO

TODO:
  - Merge the code with wiki_tmnt
  - DynamoDB
  - Save all the titles we've used before to prevent reruns
  - CI
