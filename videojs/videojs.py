""" videojsXBlock main Python class"""

import codecs
import os
import uuid

import pkg_resources
from django.conf import settings
from django.template import Context, Template
from pycaption import detect_format
from pycaption.webvtt import WebVTTWriter
from xblock.completable import XBlockCompletionMode
from xblock.core import XBlock
from xblock.fields import Boolean, Scope, String
from xblock.fragment import Fragment

@XBlock.wants('completion')
class videojsXBlock(XBlock):
    '''
    Icon of the XBlock. Values : [other (default), video, problem]
    '''
    icon_class = "video"
    completion_mode = XBlockCompletionMode.COMPLETABLE

    '''
    Fields
    '''
    display_name = String(display_name="Display Name",
                          default="Video JS",
                          scope=Scope.settings,
                          help="This name appears in the horizontal navigation at the top of the page.")

    url = String(display_name="Youtube URL or Navoica movie ID",
                 default="7b465d7b-6118-4b8a-80cd-3f40748fab74",
                 scope=Scope.content,
                 help="Enter url from website youtube.com or use id number previously uploaded movie")

    allow_download = Boolean(display_name="Video Download Allowed",
                             default=False,
                             scope=Scope.content,
                             help="Allow students to download this video.")

    source_text = String(display_name="Source document button text",
                         default="",
                         scope=Scope.content,
                         help="Add a download link for the source file of your video. Use it for example to provide the PowerPoint or PDF file used for this video.")

    subtitle_text = String(display_name="Subtitle - Polish",
                           default="",
                           scope=Scope.content,
                           help="Paste subtitles VVT")

    subtitle_url = String(display_name="Subtitle - URL - Polish",
                          default="",
                          scope=Scope.content,
                          help="")

    source_url = String(display_name="Source document URL",
                        default="",
                        scope=Scope.content,
                        help="Add a download link for the source file of your video. Use it for example to provide the PowerPoint or PDF file used for this video.")

    start_time = String(display_name="Start time",
                        default="",
                        scope=Scope.content,
                        help="The start and end time of your video. Equivalent to 'video.mp4#t=startTime,endTime' in the url.")

    end_time = String(display_name="End time",
                      default="",
                      scope=Scope.content,
                      help="The start and end time of your video. Equivalent to 'video.mp4#t=startTime,endTime' in the url.")

    '''
    Util functions
    '''

    def load_resource(self, resource_path):
        """
        Gets the content of a resource
        """
        resource_content = pkg_resources.resource_string(__name__,
                                                         resource_path)
        return unicode(resource_content)

    def render_template(self, template_path, context={}):
        """
        Evaluate a template by resource path, applying the provided context
        """
        template_str = self.load_resource(template_path)
        return Template(template_str).render(Context(context))

    '''
    Main functions
    '''

    def student_view(self, context=None):
        """
        The primary view of the XBlock, shown to students
        when viewing courses.
        """
        fullUrl = self.url
        if self.start_time != "" and self.end_time != "":
            fullUrl += "#t=" + self.start_time + "," + self.end_time
        elif self.start_time != "":
            fullUrl += "#t=" + self.start_time
        elif self.end_time != "":
            fullUrl += "#t=0," + self.end_time

        context = {
            'display_name': self.display_name,
            'url': fullUrl.strip(),
            'allow_download': self.allow_download,
            'source_text': self.source_text,
            'subtitle_url': self.subtitle_url,
            'source_url': self.source_url
        }
        html = self.render_template('static/html/videojs_view.html', context)

        frag = Fragment(html)
        frag.add_css(self.load_resource("static/css/video-js.css"))
        frag.add_css(self.load_resource("static/css/qualityselector.css"))
        frag.add_javascript(self.load_resource("static/js/video.js"))
        frag.add_javascript(self.load_resource("static/js/pl.js"))
        frag.add_javascript(self.load_resource("static/js/qualityselector.js"))
        frag.add_javascript(self.load_resource("static/js/youtube.js"))
        frag.add_javascript(self.load_resource("static/js/videojs_view.js"))
        frag.initialize_js('videojsXBlockInitView')
        return frag

    def studio_view(self, context=None):
        """
        The secondary view of the XBlock, shown to teachers
        when editing the XBlock.
        """
        context = {
            'display_name': self.display_name,
            'url': self.url.strip(),
            'allow_download': self.allow_download,
            'source_text': self.source_text,
            'source_url': self.source_url.strip(),
            'subtitle_text': self.subtitle_text,
            'subtitle_url': self.subtitle_url,
            'start_time': self.start_time,
            'end_time': self.end_time
        }
        html = self.render_template('static/html/videojs_edit.html', context)

        frag = Fragment(html)
        frag.add_javascript(self.load_resource("static/js/videojs_edit.js"))
        frag.initialize_js('videojsXBlockInitStudio')
        return frag

    @XBlock.json_handler
    def save_videojs(self, data, suffix=''):
        """
        The saving handler.
        """
        self.display_name = data['display_name']
        self.url = data['url'].strip()
        self.allow_download = True if data[
                                          'allow_download'] == "True" else False  # Str to Bool translation
        self.source_text = data['source_text']

        if not os.path.exists(settings.MEDIA_ROOT + 'subtitle/polish/'):
            os.makedirs(settings.MEDIA_ROOT + 'subtitle/polish/')

        self.subtitle_url = ''
        if data['subtitle_text']:
            reader = detect_format(data['subtitle_text'])
            if reader:
                subtitle = WebVTTWriter().write(
                    reader().read(data['subtitle_text']))

                filename = str(uuid.uuid4())

                f = codecs.open(
                    settings.MEDIA_ROOT + 'subtitle/polish/' + filename, 'w',
                    'utf-8')
                f.write(subtitle)
                f.close()

                self.subtitle_url = settings.MEDIA_URL + 'subtitle/polish/' + filename

        self.source_url = data['source_url'].strip()
        self.subtitle_text = data['subtitle_text']
        self.start_time = ''.join(
            data['start_time'].split())  # Remove whitespace
        self.end_time = ''.join(data['end_time'].split())  # Remove whitespace

        return {
            'result': 'success',
        }
