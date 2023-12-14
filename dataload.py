import os
import json
import numpy as np
import pysubs2
import pysrt

def preprocess_subtitle(text):
    text = text.replace('\n', '. ').replace('|', '').replace('{\\i1}', '').replace('{\\i0}', '').replace('\\N', '. ')
    if text.startswith('"') and text.endswith('"'):
        text = text[1:-1]
    if text.startswith("'") and text.endswith("'"):
        text = text[1:-1]
    text = text.replace('.. ', '. ')
    return text

def read_subs(path):
    subs = []
    if path.endswith('.srt') or path.endswith('.ass'):
        try:
            data = pysubs2.load(path)
            for l in data:
                subs.append(preprocess_subtitle(l.text))
        except:
            subs = []
            try:
                if path.endswith('.srt'):
                   sub_data = pysrt.open(path)
                   for sub in sub_data:
                       subs.append(preprocess_subtitle(sub.text))
            except:
                subs = []
    elif path.endswith('.sub'):
        ## https://en.wikipedia.org/wiki/MicroDVD
        with open(path, 'r') as rf:
            for l in rf:
                text = l.strip().split('}')[-1]
                subs.append(preprocess_subtitle(text))
    #if path.endswith('.srt1'):
    #    sub_data = pysrt.open(path)
    #    for sub in sub_data:
    #        subs.append(preprocess_subtitle(sub.text))
    return subs

# path = '/home/lokesh/data/nlp/Subtitles/english/badal.(2000)/Badal 2000 1080p AMZN WEB-DL DDP2.0 H264-PHDM.srt'
# path = '/home/lokesh/data/nlp/Subtitles/english/the.english.patient.(1996)/The English patient (1996).eng.1080p.ass'
# path = '/home/lokesh/data/nlp/Subtitles/english/beyond.the.law.(1993)/Fixing.the.Shadow.1993.Directors.Cut.iNTERNAL.1080p.BluRay.x264-WaLMaRT.sub'