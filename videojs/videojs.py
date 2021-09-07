""" videojsXBlock main Python class"""

import codecs
import os
import uuid
from html.parser import HTMLParser

import pkg_resources
from django.conf import settings
from django.template import Context, Template
from pycaption import detect_format
from pycaption.webvtt import WebVTTWriter
from xblock.core import XBlock
from xblock.fields import Scope, String, Dict
from xblock.fragment import Fragment
from xblockutils.resources import ResourceLoader
from webob import Response
import json
import hashlib
from django.utils import translation
from six import text_type

_ = lambda text: text
loader = ResourceLoader(__name__)


@XBlock.needs('i18n')
@XBlock.wants('completion')
class videojsXBlock(XBlock):
    '''
    Icon of the XBlock. Values : [other (default), video, problem]
    '''
    icon_class = "video"

    languages = {
        'pl': _('Polish'),
        'en': _('English'),
        'de': _('German'),
        'fr': _('French'),
        'it': _('Italian'),
        'uk': _('Ukrainian'),
        'aa': _('Afar'),
        'ab': _('Abkhazian'),
        'af': _('Afrikaans'),
        'ak': _('Akan'),
        'sq': _('Albanian'),
        'am': _('Amharic'),
        'ar': _('Arabic'),
        'an': _('Aragonese'),
        'hy': _('Armenian'),
        'as': _('Assamese'),
        'av': _('Avaric'),
        'ae': _('Avestan'),
        'ay': _('Aymara'),
        'az': _('Azerbaijani'),
        'ba': _('Bashkir'),
        'bm': _('Bambara'),
        'eu': _('Basque'),
        'be': _('Belarusian'),
        'bn': _('Bengali'),
        'bh': _('Bihari languages'),
        'bi': _('Bislama'),
        'bo': _('Tibetan'),
        'bs': _('Bosnian'),
        'br': _('Breton'),
        'bg': _('Bulgarian'),
        'my': _('Burmese'),
        'ca': _('Catalan; Valencian'),
        'cs': _('Czech'),
        'ch': _('Chamorro'),
        'ce': _('Chechen'),
        'zh': _('Chinese'),
        'cu': _('Church Slavic; Old Slavonic; Church Slavonic; Old Bulgarian; Old Church Slavonic'),
        'cv': _('Chuvash'),
        'kw': _('Cornish'),
        'co': _('Corsican'),
        'cr': _('Cree'),
        'cy': _('Welsh'),
        'da': _('Danish'),
        'dv': _('Divehi; Dhivehi; Maldivian'),
        'nl': _('Dutch; Flemish'),
        'dz': _('Dzongkha'),
        'el': _('Greek, Modern (1453-)'),
        'eo': _('Esperanto'),
        'et': _('Estonian'),
        'ee': _('Ewe'),
        'fo': _('Faroese'),
        'fj': _('Fijian'),
        'fi': _('Finnish'),
        'fy': _('Western Frisian'),
        'ff': _('Fulah'),
        'Ga': _('Georgian'),
        'gd': _('Gaelic; Scottish Gaelic'),
        'ga': _('Irish'),
        'gl': _('Galician'),
        'gv': _('Manx'),
        'gn': _('Guarani'),
        'gu': _('Gujarati'),
        'ht': _('Haitian; Haitian Creole'),
        'ha': _('Hausa'),
        'he': _('Hebrew'),
        'hz': _('Herero'),
        'hi': _('Hindi'),
        'ho': _('Hiri Motu'),
        'hr': _('Croatian'),
        'hu': _('Hungarian'),
        'ig': _('Igbo'),
        'is': _('Icelandic'),
        'io': _('Ido'),
        'ii': _('Sichuan Yi; Nuosu'),
        'iu': _('Inuktitut'),
        'ie': _('Interlingue; Occidental'),
        'ia': _('Interlingua (International Auxiliary Language Association)'),
        'id': _('Indonesian'),
        'ik': _('Inupiaq'),
        'jv': _('Javanese'),
        'ja': _('Japanese'),
        'kl': _('Kalaallisut; Greenlandic'),
        'kn': _('Kannada'),
        'ks': _('Kashmiri'),
        'ka': _('Georgian'),
        'kr': _('Kanuri'),
        'kk': _('Kazakh'),
        'km': _('Central Khmer'),
        'ki': _('Kikuyu; Gikuyu'),
        'rw': _('Kinyarwanda'),
        'ky': _('Kirghiz; Kyrgyz'),
        'kv': _('Komi'),
        'kg': _('Kongo'),
        'ko': _('Korean'),
        'kj': _('Kuanyama; Kwanyama'),
        'ku': _('Kurdish'),
        'lo': _('Lao'),
        'la': _('Latin'),
        'lv': _('Latvian'),
        'li': _('Limburgan; Limburger; Limburgish'),
        'ln': _('Lingala'),
        'lt': _('Lithuanian'),
        'lb': _('Luxembourgish; Letzeburgesch'),
        'lu': _('Luba-Katanga'),
        'lg': _('Ganda'),
        'mk': _('Macedonian'),
        'mh': _('Marshallese'),
        'ml': _('Malayalam'),
        'mi': _('Maori'),
        'mr': _('Marathi'),
        'ms': _('Malay'),
        'Mi': _('Micmac'),
        'mg': _('Malagasy'),
        'mt': _('Maltese'),
        'mn': _('Mongolian'),
        'na': _('Nauru'),
        'nv': _('Navajo; Navaho'),
        'nr': _('Ndebele, South; South Ndebele'),
        'nd': _('Ndebele, North; North Ndebele'),
        'ng': _('Ndonga'),
        'ne': _('Nepali'),
        'nn': _('Norwegian Nynorsk; Nynorsk, Norwegian'),
        'nb': _('Bokmål, Norwegian; Norwegian Bokmål'),
        'no': _('Norwegian'),
        'oc': _('Occitan (post 1500)'),
        'oj': _('Ojibwa'),
        'or': _('Oriya'),
        'om': _('Oromo'),
        'os': _('Ossetian; Ossetic'),
        'pa': _('Panjabi; Punjabi'),
        'fa': _('Persian'),
        'pi': _('Pali'),
        'pt': _('Portuguese'),
        'ps': _('Pushto; Pashto'),
        'qu': _('Quechua'),
        'rm': _('Romansh'),
        'ro': _('Romanian; Moldavian; Moldovan'),
        'rn': _('Rundi'),
        'ru': _('Russian'),
        'sg': _('Sango'),
        'sa': _('Sanskrit'),
        'si': _('Sinhala; Sinhalese'),
        'sk': _('Slovak'),
        'sl': _('Slovenian'),
        'se': _('Northern Sami'),
        'sm': _('Samoan'),
        'sn': _('Shona'),
        'sd': _('Sindhi'),
        'so': _('Somali'),
        'st': _('Sotho, Southern'),
        'es': _('Spanish; Castilian'),
        'sc': _('Sardinian'),
        'sr': _('Serbian'),
        'ss': _('Swati'),
        'su': _('Sundanese'),
        'sw': _('Swahili'),
        'sv': _('Swedish'),
        'ty': _('Tahitian'),
        'ta': _('Tamil'),
        'tt': _('Tatar'),
        'te': _('Telugu'),
        'tg': _('Tajik'),
        'tl': _('Tagalog'),
        'th': _('Thai'),
        'ti': _('Tigrinya'),
        'to': _('Tonga (Tonga Islands)'),
        'tn': _('Tswana'),
        'ts': _('Tsonga'),
        'tk': _('Turkmen'),
        'tr': _('Turkish'),
        'tw': _('Twi'),
        'ug': _('Uighur; Uyghur'),
        'ur': _('Urdu'),
        'uz': _('Uzbek'),
        've': _('Venda'),
        'vi': _('Vietnamese'),
        'vo': _('Volapük'),
        'wa': _('Walloon'),
        'wo': _('Wolof'),
        'xh': _('Xhosa'),
        'yi': _('Yiddish'),
        'yo': _('Yoruba'),
        'za': _('Zhuang; Chuang'),
        'zu': _('Zulu')
    }

    '''
    Fields
    '''
    display_name = String(display_name=_("Display Name"),
                          default=_("Video JS"),
                          scope=Scope.settings)

    url = String(display_name=_("Youtube URL or Navoica movie ID"),
                 default="7b465d7b-6118-4b8a-80cd-3f40748fab74",
                 scope=Scope.content,
                 help=_("Enter url from website youtube.com or use id number previously uploaded movie"))

    # old fallback
    subtitle_text = String(display_name=_("Subtitle - Polish"),
                           default="",
                           scope=Scope.content,
                           help=_("Paste subtitles VTT"))

    # old fallback
    subtitle_url = String(display_name=_("Subtitle - URL - Polish"),
                          default="",
                          scope=Scope.content,
                          help="")

    subtitles = Dict(display_name=_("Subtitles RAW"),
                     default={},
                     scope=Scope.content
                     )

    subtitles_url = Dict(display_name=_("Subtitles URL"),
                         default={},
                         scope=Scope.content
                         )

    def load_resource(self, resource_path):
        """
        Gets the content of a resource
        """
        resource_content = pkg_resources.resource_string(__name__,
                                                         resource_path)
        return text_type(resource_content)

    def render_template(self, template_path, context={}):
        """
        Evaluate a template by resource path, applying the provided context
        """
        template_str = loader.load_unicode(template_path)
        return Template(template_str).render(Context(context))

    '''
    Main functions
    '''

    def student_view(self, context=None):
        """
        The primary view of the XBlock, shown to students
        when viewing courses.
        """

        subtitles_url = {}
        for lang, subtitle_text in dict(self.subtitles).items():
            file = self.create_subtitles_file(subtitle_text)
            if file:
                subtitles_url[lang] = file

        if len(subtitles_url.get("pl", "")) == 0 and self.subtitle_url:
            """Stara wersja zawierala jedynie napisy w jezyku PL. Dlatego musimy byc wsteczni kompatybilni"""
            subtitles_url['pl'] = self.subtitle_url

        frag = Fragment()

        context = {
            'display_name': self.display_name,
            'url': self.url,
            'uid': uuid.uuid4().hex,
            'subtitles_url': subtitles_url,
        }

        frag.add_content(loader.render_django_template(
            'static/html/videojs_view.html',
            context=context,
            i18n_service=self.runtime.service(self, "i18n"),
        ))

        frag.add_css(loader.load_unicode("static/css/video-js.css"))
        frag.add_css(loader.load_unicode("static/css/qualityselector.css"))
        frag.add_javascript(loader.load_unicode("static/js/video.js"))
        frag.add_javascript(loader.load_unicode("static/js/pl.js"))
        frag.add_javascript(loader.load_unicode("static/js/qualityselector.js"))
        frag.add_javascript(loader.load_unicode("static/js/youtube.js"))
        frag.add_javascript(loader.load_unicode("static/js/videojs_view.js"))
        frag.add_javascript(self.get_translation_content())

        frag.initialize_js('videojsXBlockInitView')
        return frag

    def studio_view(self, context=None):

        if not 'pl' in self.subtitles and self.subtitle_url:
            if os.path.isfile(self.subtitle_url):
                with open(self.subtitle_url, 'r') as f:
                    data = f.read()
                    self.subtitles['pl'] = data
            elif self.subtitle_text:
                reader = detect_format(self.subtitle_text)
                if reader:
                    subtitle = WebVTTWriter().write(reader().read(self.subtitle_text))
                    h = HTMLParser()
                    self.subtitles['pl'] = h.unescape(subtitle)
                    self.create_subtitles_file(self.subtitles['pl'])

        languages_subtitles = {code: {'name': self.languages[code], 'subtitle': self.subtitles.get(code, '')} for code
                               in
                               self.languages.keys()}

        context = {
            'display_name': self.display_name,
            'url': self.url.strip(),
            'languages': languages_subtitles,
            'subtitles': self.subtitles,
        }

        frag = Fragment()

        frag.add_content(loader.render_django_template(
            'static/html/videojs_edit.html',
            context=context,
            i18n_service=self.runtime.service(self, "i18n"),
        ))

        frag.add_javascript(self.get_translation_content())
        frag.add_javascript(loader.load_unicode("static/js/videojs_edit.js"))
        frag.initialize_js('videojsXBlockInitStudio')
        return frag

    @XBlock.json_handler
    def save_videojs(self, data, suffix=''):
        """
        The saving handler.
        """
        i18n_ = self.runtime.service(self, "i18n").ugettext

        self.display_name = data['display_name']
        self.url = data['url'].strip()

        for language in self.languages.keys():
            subtitle_text = data['subtitle_text_' + language].strip()
            if subtitle_text:
                reader = detect_format(subtitle_text)
                if reader:
                    subtitle = WebVTTWriter().write(reader().read(subtitle_text))
                    h = HTMLParser()
                    self.subtitles[language] = h.unescape(subtitle)

                    self.create_subtitles_file(self.subtitles[language])
                else:
                    return Response(json.dumps(
                        {'error': i18n_(
                            "Error occurred while saving VTT subtitles for language %s") % language.upper()}),
                        status=400, content_type='application/json', charset='utf8')
            else:
                self.subtitles[language] = ""
                # We need to remove the old url for Polish subtitles so that they will not be re-imported
                if language == 'pl' and self.subtitle_url:
                    self.subtitle_url = None

        return {'result': 'success'}

    def create_subtitles_file(self, subtitle_text):
        if subtitle_text:
            path = settings.MEDIA_ROOT + 'subtitles/'
            if not os.path.exists(path):
                os.makedirs(path)

            name = hashlib.sha256(subtitle_text.encode("utf-8")).hexdigest() + ".vtt"
            filepath = path + name
            url = settings.MEDIA_URL + 'subtitles/' + name

            if not os.path.isfile(filepath):
                try:
                    f = codecs.open(filepath, 'w', 'utf-8')
                    f.write(subtitle_text)
                    f.close()
                except IOError:
                    return None
            return url
        return None

    def resource_string(self, path):
        data = pkg_resources.resource_string(__name__, path)
        return data.decode('utf8')

    def get_translation_content(self):
        try:
            return self.resource_string('static/js/translations/{lang}/text.js'.format(
                lang=translation.get_language(),
            ))
        except IOError:
            return self.resource_string('static/js/translations/en/text.js')
