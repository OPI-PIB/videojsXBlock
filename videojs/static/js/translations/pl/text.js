
            (function(global){
                var videojsi18n = {
                  init: function() {
                    

(function(globals) {

  var django = globals.django || (globals.django = {});

  
  django.pluralidx = function(n) {
    var v=(n==1 ? 0 : (n%10>=2 && n%10<=4) && (n%100<12 || n%100>14) ? 1 : n!=1 && (n%10>=0 && n%10<=1) || (n%10>=5 && n%10<=9) || (n%100>=12 && n%100<=14) ? 2 : 3);
    if (typeof(v) == 'boolean') {
      return v ? 1 : 0;
    } else {
      return v;
    }
  };
  

  /* gettext library */

  django.catalog = django.catalog || {};
  
  var newcatalog = {
    "Abkhazian": "abchaski",
    "Add": "Dodaj",
    "Add new language": "Dodaj nowy j\u0119zyk",
    "Afar": "afar",
    "Afrikaans": "afrikaans",
    "Akan": "akan",
    "Albanian": "alba\u0144ski",
    "Amharic": "amharski",
    "Arabic": "arabski",
    "Aragonese": "arago\u0144ski",
    "Armenian": "ormia\u0144ski",
    "Assamese": "asamski",
    "Avaric": "awarski",
    "Avestan": "awestyjski",
    "Aymara": "ajmarski",
    "Azerbaijani": "azerbejd\u017ca\u0144ski",
    "Bambara": "bambara",
    "Bashkir": "baszkirski",
    "Basque": "baskijski",
    "Belarusian": "bia\u0142oruski",
    "Bengali": "bengalski",
    "Bihari languages": "biharski",
    "Bislama": "bislama",
    "Bokm\u00e5l, Norwegian; Norwegian Bokm\u00e5l": "bokm\u00e5l, norweski",
    "Bosnian": "bo\u015bniacki",
    "Breton": "breto\u0144ski",
    "Bulgarian": "bu\u0142garski",
    "Burmese": "burma\u0144ski",
    "Cancel": "Anuluj",
    "Catalan; Valencian": "katalo\u0144ski",
    "Central Khmer": "khmerski",
    "Chamorro": "czamorro ",
    "Chechen": "czecze\u0144ski",
    "Chinese": "chi\u0144ski",
    "Church Slavic; Old Slavonic; Church Slavonic; Old Bulgarian; Old Church Slavonic": "staros\u0142owia\u0144ski",
    "Chuvash": "czuwaski",
    "Cornish": "kornwalijski",
    "Corsican": "korsyka\u0144ski",
    "Cree": "kri",
    "Croatian": "chorwacki",
    "Czech": "czeski",
    "Danish": "du\u0144ski",
    "Display Name": "Nazwa",
    "Display name": "Nazwa",
    "Divehi; Dhivehi; Maldivian": "malediwski",
    "Dutch; Flemish": "niderlandzki\u00a0",
    "Dzongkha": "dzongkha",
    "English": "angielski",
    "Enter url from website youtube.com or use id number previously uploaded movie": "Wpisz adres URL ze strony youtube.com lub u\u017cyj numeru identyfikacyjnego przes\u0142anego wcze\u015bniej filmu",
    "Esperanto": "esperanto",
    "Estonian": "esto\u0144ski",
    "Ewe": "ewe",
    "Faroese": "farerski",
    "Fijian": "fid\u017cyjski",
    "Finnish": "fi\u0144ski",
    "French": "francuski",
    "Fulah": "ful",
    "Gaelic; Scottish Gaelic": "celtycki",
    "Galician": "galisyjski",
    "Ganda": "ganda",
    "Georgian": "gruzi\u0144ski",
    "German": "niemiecki",
    "Greek, Modern (1453-)": "grecki (1453-)",
    "Guarani": "guarani",
    "Gujarati": "gud\u017carati",
    "Haitian; Haitian Creole": "haita\u0144ski",
    "Hausa": "hausa",
    "Hebrew": "hebrajski",
    "Herero": "herero",
    "Hindi": "hindi",
    "Hiri Motu": "hiri motu",
    "Hungarian": "w\u0119gierski",
    "Icelandic": "islandzki",
    "Ido": "ido",
    "Igbo": "ibo",
    "Indonesian": "indonezyjski",
    "Interlingua (International Auxiliary Language Association)": "interlingua (International Auxiliary Language Association)",
    "Interlingue; Occidental": "interlingue",
    "Inuktitut": "inuktitut",
    "Inupiaq": "inupiak",
    "Irish": "irlandzki",
    "Italian": "w\u0142oski",
    "Japanese": "japo\u0144ski",
    "Javanese": "jawajski",
    "Kalaallisut; Greenlandic": "grenlandzki",
    "Kannada": "kannada",
    "Kanuri": "kanuri",
    "Kashmiri": "kaszmirski",
    "Kazakh": "kazachski",
    "Kikuyu; Gikuyu": "kikuju",
    "Kinyarwanda": "kinyarwanda",
    "Kirghiz; Kyrgyz": "kirgiski",
    "Komi": "komi",
    "Kongo": "kongo",
    "Korean": "korea\u0144ski",
    "Kuanyama; Kwanyama": "kwanyama",
    "Kurdish": "kurdyjski",
    "Language": "J\u0119zyk",
    "Lao": "laota\u0144ski",
    "Latin": "\u0142acina",
    "Latvian": "\u0142otewski",
    "Limburgan; Limburger; Limburgish": "limburski",
    "Lingala": "lingala",
    "Lithuanian": "litewski",
    "Luba-Katanga": "luba-katanga",
    "Luxembourgish; Letzeburgesch": "luksemburski",
    "Macedonian": "macedo\u0144ski",
    "Malagasy": "malgaski",
    "Malay": "malajski",
    "Malayalam": "malajalam",
    "Maltese": "malta\u0144ski",
    "Manx": "ma\u0144ski",
    "Maori": "maoryski",
    "Marathi": "marathi",
    "Marshallese": "marszalski",
    "Micmac": "mikmak",
    "Mongolian": "mongolski",
    "Movie URL/ID": "Film URL lub ID",
    "Nauru": "naura\u0144ski",
    "Navajo; Navaho": "Nawaho",
    "Ndebele, North; North Ndebele": "ndebele p\u00f3\u0142nocny",
    "Ndebele, South; South Ndebele": "ndebele po\u0142udniowy",
    "Ndonga": "ndonga",
    "Nepali": "nepalski",
    "Northern Sami": "p\u00f3\u0142nocnosaamski",
    "Norwegian": "norweski",
    "Norwegian Nynorsk; Nynorsk, Norwegian": "nynorsk, norweski",
    "Occitan (post 1500)": "prowansalski (po 1500)",
    "Ojibwa": "ojibwa",
    "Oriya": "orija",
    "Oromo": "oromo",
    "Ossetian; Ossetic": "osetyjski",
    "Pali": "pali",
    "Panjabi; Punjabi": "pend\u017cabski",
    "Paste VTT subtitles text": "Wklej napisy w formacie VTT",
    "Paste subtitles VTT": "Wklej napisy VTT",
    "Persian": "perski",
    "Polish": "polski",
    "Portuguese": "portugalski",
    "Pushto; Pashto": "paszto",
    "Quechua": "keczua",
    "Remove": "Usu\u0144",
    "Romanian; Moldavian; Moldovan": "rumu\u0144ski",
    "Romansh": "romansz",
    "Rundi": "rundi",
    "Russian": "rosyjski",
    "Samoan": "samoa\u0144ski",
    "Sango": "sango",
    "Sanskrit": "sanskryt",
    "Sardinian": "sardy\u0144ski",
    "Save": "Zapisz",
    "Serbian": "serbski",
    "Shona": "shona",
    "Sichuan Yi; Nuosu": "nuosu",
    "Sindhi": "sindhi",
    "Sinhala; Sinhalese": "syngaleski",
    "Slovak": "s\u0142owacki",
    "Slovenian": "s\u0142owe\u0144ski",
    "Somali": "somalijski",
    "Sotho, Southern": "sotho",
    "Spanish; Castilian": "hiszpa\u0144ski",
    "Subtitle - Polish": "Napisy polskie",
    "Subtitle - URL - Polish": "Napisy - adres URL - polskie",
    "Subtitles RAW": "Napisy RAW",
    "Subtitles URL": "Napisy URLe",
    "Sundanese": "sundajski",
    "Swahili": "suahili",
    "Swati": "swati",
    "Swedish": "szwedzki",
    "Tagalog": "tagalski",
    "Tahitian": "tahita\u0144ski",
    "Tajik": "tad\u017cycki",
    "Tamil": "tamilski",
    "Tatar": "tatarski",
    "Telugu": "telugu",
    "Thai": "tajski",
    "Tibetan": "tybeta\u0144ski",
    "Tigrinya": "tigrinia",
    "Tonga (Tonga Islands)": "tonga (wyspy Tonga)",
    "Tsonga": "tsonga\u00a0",
    "Tswana": "tswana",
    "Turkish": "turecki",
    "Turkmen": "turkme\u0144ski",
    "Twi": "twi",
    "Type in movie id for uploader or paste youtube link": "Wpisz numer ID filmu z panelu do przesy\u0142ania film\u00f3w lub wklej link do serwisu YouTube",
    "Uighur; Uyghur": "ujgurski",
    "Ukrainian": "ukrai\u0144ski",
    "Urdu": "urdu",
    "Uzbek": "uzbecki",
    "Venda": "venda",
    "Video JS": "Video JS",
    "Vietnamese": "wietnamski",
    "Volap\u00fck": "Volap\u00fck",
    "Walloon": "walo\u0144ski",
    "Welsh": "walijski",
    "Western Frisian": "zachodniofryzyjski",
    "Wolof": "wolof",
    "Xhosa": "xhosa",
    "Yiddish": "jidysz",
    "Yoruba": "joruba",
    "Youtube URL or Navoica movie ID": "Adres Youtube lub ID filmu z Navoica.pl",
    "Zhuang; Chuang": "zhuang",
    "Zulu": "zuluski"
  };
  for (var key in newcatalog) {
    django.catalog[key] = newcatalog[key];
  }
  

  if (!django.jsi18n_initialized) {
    django.gettext = function(msgid) {
      var value = django.catalog[msgid];
      if (typeof(value) == 'undefined') {
        return msgid;
      } else {
        return (typeof(value) == 'string') ? value : value[0];
      }
    };

    django.ngettext = function(singular, plural, count) {
      var value = django.catalog[singular];
      if (typeof(value) == 'undefined') {
        return (count == 1) ? singular : plural;
      } else {
        return value[django.pluralidx(count)];
      }
    };

    django.gettext_noop = function(msgid) { return msgid; };

    django.pgettext = function(context, msgid) {
      var value = django.gettext(context + '\x04' + msgid);
      if (value.indexOf('\x04') != -1) {
        value = msgid;
      }
      return value;
    };

    django.npgettext = function(context, singular, plural, count) {
      var value = django.ngettext(context + '\x04' + singular, context + '\x04' + plural, count);
      if (value.indexOf('\x04') != -1) {
        value = django.ngettext(singular, plural, count);
      }
      return value;
    };

    django.interpolate = function(fmt, obj, named) {
      if (named) {
        return fmt.replace(/%\(\w+\)s/g, function(match){return String(obj[match.slice(2,-2)])});
      } else {
        return fmt.replace(/%s/g, function(match){return String(obj.shift())});
      }
    };


    /* formatting library */

    django.formats = {
    "DATETIME_FORMAT": "j E Y H:i",
    "DATETIME_INPUT_FORMATS": [
      "%d.%m.%Y %H:%M:%S",
      "%d.%m.%Y %H:%M:%S.%f",
      "%d.%m.%Y %H:%M",
      "%d.%m.%Y",
      "%Y-%m-%d %H:%M:%S",
      "%Y-%m-%d %H:%M:%S.%f",
      "%Y-%m-%d %H:%M",
      "%Y-%m-%d"
    ],
    "DATE_FORMAT": "j E Y",
    "DATE_INPUT_FORMATS": [
      "%d.%m.%Y",
      "%d.%m.%y",
      "%y-%m-%d",
      "%Y-%m-%d"
    ],
    "DECIMAL_SEPARATOR": ",",
    "FIRST_DAY_OF_WEEK": "1",
    "MONTH_DAY_FORMAT": "j F",
    "NUMBER_GROUPING": "3",
    "SHORT_DATETIME_FORMAT": "d-m-Y  H:i",
    "SHORT_DATE_FORMAT": "d-m-Y",
    "THOUSAND_SEPARATOR": "\u00a0",
    "TIME_FORMAT": "H:i",
    "TIME_INPUT_FORMATS": [
      "%H:%M:%S",
      "%H:%M:%S.%f",
      "%H:%M"
    ],
    "YEAR_MONTH_FORMAT": "F Y"
  };

    django.get_format = function(format_type) {
      var value = django.formats[format_type];
      if (typeof(value) == 'undefined') {
        return format_type;
      } else {
        return value;
      }
    };

    /* add to global namespace */
    globals.pluralidx = django.pluralidx;
    globals.gettext = django.gettext;
    globals.ngettext = django.ngettext;
    globals.gettext_noop = django.gettext_noop;
    globals.pgettext = django.pgettext;
    globals.npgettext = django.npgettext;
    globals.interpolate = django.interpolate;
    globals.get_format = django.get_format;

    django.jsi18n_initialized = true;
  }

}(this));


                  }
                };
                videojsi18n.init();
                global.videojsi18n = videojsi18n;
            }(this));
        