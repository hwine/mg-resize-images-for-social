# mg-resize-images-for-social
script/app to be resize images to ones needed by various social media sites

Any format image can be supplied as input. All outputs are in JPEG
format.

Every image is output in all formats -- delete the ones you don't need.
The target site is indicted by a string appended to the filename. See
table for currently supported sizes.

| Service   |  suffix | pixels |
|-----|:------:|:-----:|
| Instagram  |  ig  |  108 x 1080  |
| Facebook  |  fb  |  120 x 630  |
| FB_event  |  fbe  |  192 x 630  |
| EventBrite  |  eb  |  216 x 1080  |
| Twitter  |  tw  |  108 x 1080  |
| Nextdoor  |  nd  |  70 x 240  |
| Patch  |  pch  |  120 x 900  |


# Dev

Currently, app is only generated for MacOS. See the
[pyinstaller][pyinstaller] docs for details.

The script is turned into any app with the help of two tools:
1. [Gooey][gooey] to provide the windowed interface.
2. [pyinstaller][pyinstaller] to package as an app.


<!-- references -->
[Gooey]: https://github.com/chriskiehl/Gooey
[pyinstaller]: https://github.com/pyinstaller/pyinstaller
