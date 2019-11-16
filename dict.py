#!/usr/bin/env python
#-*- coding:utf-8 -*-
import sys
import DictionaryServices
import re

split_words = ['PHRASES', 'ORIGIN', 'DERIVATIVES']
#'noun ', 'preposition ', 'verb ', 'abbreviation ', 'adjective ']
def main():
    try:
        search_term = sys.argv[1].decode('utf-8')
    except IndexError:
        print('No search term was entered.')
        sys.exit()
    search_result = DictionaryServices.DCSCopyTextDefinition(None, search_term, (0, len(search_term)))
    if not search_result:
        errmsg = '"%s" was not found in Dictionary.' % (search_term)
        print(errmsg.encode('utf-8'))
    else:
        for word in split_words:
            search_result = search_result.replace(word, '\r\n'+word+'\r\n')
        search_result = re.sub(r" (\d+) ", r"\r\n\1 ", search_result, re.MULTILINE)
        search_result = re.sub(ur"\u25B6(\w+)\b", r"\r\n\1: ", search_result, re.MULTILINE|re.UNICODE)
        search_result = search_result.replace(u'\u2022', u'\r\n    \u2022')
        print(search_result)

if __name__ == '__main__':
    main()
