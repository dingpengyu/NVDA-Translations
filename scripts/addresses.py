# -*- coding: utf-8 -*-
import sys
from subprocess import PIPE, Popen

addresses = {
    'all': {
        'lang': 'all',
        'email': ['Mesar hameed <mesar.hameed@gmail.com>'], 
    },
    'ar': { 
        'lang':'Arabic',
        'email': ['Fatma Mehanna <fatma.mehanna@gmail.com>'],
    },
    'bg': {
        'lang':'Bulgarian',
        'email': ['Zahari Yurukov <zahari.yurukov@gmail.com>'],
    },
'cz': {
        'lang': 'Czech',
        'email': ['Radek zalud <radek.zalud@seznam.cz>'],
    },
    'da': {
        'lang': 'Danish',
        'email': ['Daniel K. Gartmann <kontakt@nvda.dk>'],
    },
    'de': {
        'lang':'German',
        'email': ['Bernd Dorer <bernd_dorer@yahoo.de>', 'David Parduhn <xkill85@gmx.net>'],
    },
    'el': {
        'lang': 'Greek',
        'email': ['access@e-rhetor.com'],
    },
    'es': {
        'lang': 'Spanish',
        'email': ['Juan C. buno <quetzatl@eresmas.net>'],
    },
    'fi': {
        'lang':'Finnish',
        'email': ['Jani Kinnunen <jani.kinnunen@wippies.fi>'],
    }, 
    'fr': {
        'lang':'French',
        'email': ['Michel such <michel.such@free.fr>'],
    },
    'gl': {
        'lang': 'Galician',
        'email': ['Juan C. buno <quetzatl@eresmas.net>'],
    },
    'hr': {
        'lang': 'Croatian',
        'email': ['Hrvoje Katic <hrvojekatic@gmail.com>', 'Mario Percinic <mario.percinic@gmail.com>'],
    },
    'hu': {
        'lang': 'Hungarian',
        'email': ['Aron OcsvAri <oaron1@gmail.com>'],
    },
    'it': {
        'lang':'Italian',
        'email': ['Simone Dal Maso <simone.dalmaso@juvox.it>'],
    },
    'ja': {
        'lang':'Japanese',
        'email': ['Katsutoshi Tsuji <tsuji-katsutoshi@mitsue.co.jp>', 'Nakamura Kiyochika <nakamura-kiyochika@mitsue.co.jp>'],
    },
    'nb_NO': {
        'lang':'Norwegian bokmål',
        'email': ['David Hole <balubathebrave@gmail.com>', 'Bjornar Seppola <bjornar@seppola.net>'],
    },
    'nl': {
        'lang':'Duch',
        'email': ['Bram Duvigneau <bram@bramd.nl>'],
    },
    'pl': {
        'lang':'Polish',
        'email': ['Hubert Meyer <killer@tyflonet.com>'],
    },
   'pt_BR': {
        'lang': 'Brazilian Portuguese',
        'email': ['Cleverson Casarin Uliana <clever92000@yahoo.com.br>', 'Marlin Rodrigues <marlincgrodrigues@yahoo.com.br>'],
    },
    'pt_PT': {
        'lang': 'Portuguese',
        'email': ['Diogo Costa <diogojoca@gmail.com>'],
    },
'sk': {
        'lang':'Slovak',
        'email': ['Ondrej Rosik <ondrej.rosik@gmail.com>', 'Peter Vagner <peter.v@datagate.sk>'],
    },
    'sv': {
        'lang':'Swedish',
        'email': ['Mesar Hameed <mhameed@src.gnome.org>'],
    },
    'ta': {
        'lang':'Tamil',
        'email': ['Dinakar T.D. <td.dinkar@gmail.com>'],
    },
    'tr': {
        'lang':'Turkish',
        'email': ['Cagri Dogan <cagrid@hotmail.com>'],
    },
    'zh_CN': {
        'lang':'Simplified Chinese',
        'email': ['qt06.com@139.com'],
    },
    'zh_HK': {
        'lang': 'Traditional Chinese Hong Kong',
        'email': ['Eric Yip <ericycy@gmail.com>'],
    },
    'zh_TW': {
        'lang': 'Traditional Chinese Taiwan',
        'email': ['wangjanli@gmail.com', 'maro.zhang@gmail.com'],
    },
}

def email(rcpts, subject, body):
    rcpts.extend(addresses['all']['email'])
    to = ", ".join(rcpts)
    p1 = Popen(['echo', '-e', body], stdout=PIPE)
    p2 = Popen(['mail', '-s', subject, to], stdin=p1.stdout)


if __name__ == "__main__" and len(sys.argv) == 4:
    lang = sys.argv[1]
    if not addresses.has_key(lang):
        print "unable to find language: %s" %lang
        sys.exit()
    email(addresses[lang]['email'], sys.argv[2], sys.argv[3])  
