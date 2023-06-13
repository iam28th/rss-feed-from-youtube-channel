import os
import sys
import urllib.request
import urllib.error
from yt_channel_parser import YtChannelParser

script_name = sys.argv[0]


def print_usage():
    s = "\n".join(["Usage:", f"$ python {script_name} -l <file_with_urls.txt>"])
    print(s)


def get_channel_id_from_url(url):
    parser = YtChannelParser()
    with urllib.request.urlopen(url) as req:
        parser.feed(req.read().decode("utf8"))
    return parser.channel_id


def get_rss_url_from_channel_id(channel_id):
    return f"https://www.youtube.com/feeds/videos.xml?channel_id={channel_id}"


if len(sys.argv) != 3:
    print_usage()
    sys.exit(1)

assert sys.argv[1] == "-l"
fn = sys.argv[2]
assert os.path.isfile(fn), f"{fn} does not exist"

with open(fn, "r") as fin:
    for line in fin:
        if "#" in line:
            line, comments = [x.split() for x in line.split("#")]
        else:
            line = line.split()
            comments = []
        try:
            channel_id = get_channel_id_from_url(line[0])
            rss_url = get_rss_url_from_channel_id(channel_id)
        except urllib.error.HTTPError as e:
            sys.stderr.write(line[0] + " " + str(e) + '\n')
            continue
        try:
            tags = line[1:]
        except IndexError:
            tags = []
        sys.stdout.write(rss_url + " ")
        sys.stdout.write(" ".join(tags) + " ")
        if comments:
            sys.stdout.write("# " + " ".join(comments))
        sys.stdout.write("\n")
