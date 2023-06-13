# Youtube Channel page parser for RSS feed
A script that converts youtube channel urls to rss feed urls
(e.g. `https://www.youtube.com/@LukeSmithxyz` to `https://www.youtube.com/feeds/videos.xml?channel_id=UC2eYFnH61tmytImy1mTYvhA`)
and prints them to stdout.

### Usage
`python rss_feed_from_youtube_channel.py -l <file_with_links.txt>`

`<file_with_links.txt>` should contain one link per line. Tags and comments for `newsboat`'s `urls` files are also supported, see `example_file_with_links.txt`.
