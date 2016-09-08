# cool-crawler
## So what is this project about?

This python script will help you to crawl webpages. It's not a generic application, but with slight modifications you can basically make it to be appropriate for your case.

The basic idea of this app for me, is to search ``demonoid`` and porbably `thepiratebay.org` with some query. The application, in this case will take the urls for the listed torrents and store them in a file ``myfile.txt`` super creative name BTW. Then I'll the relative path of the url and add them to the baseurl ``https://demonoid.pw/<relative_path>``. After that we'll visit each of the links, and search for ``href`` that starts with ``magnet`` and store them in a file ``magnets_file.txt``.

Then I'll just copy those magnet urls and put them into my prefered torrent client! Super cool isn't it?

## Future directions

Well, I'll make this program compatible with the major torrents website. I may use some functions, or classes if it's necessary. But I really just want it to solve some problem I faced, automate a very pooring stuff. Another thing which I'm very interesting in is to translate it to Bash, or even better to use Bash scripting, and Python simulataneously.

## A very final notes

To make this code compatible with your application, I'd change the ``url`` in line 4 to something like this ``https://thepiratebay.org/search/naruto/0/99/0`` which is basically saying, search results for naruto in ``all`` categories, without any sorting whatsoever.
Change line 23 in main function ``if '/files/details/' in link['href']:`` to be ``if '\torrents\' in link['href']:`` It just happened that the patterns of tpb is ``https://www.thepiratebay.org/torrents/some_digits_here`` You can use regular expression though, but I think this is fast enough.

If you find this script useful for you, fork it, pull request for any further enhancements, efficiency discussions very very welcome!
