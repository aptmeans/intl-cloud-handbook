#!/usr/bin/env python3
"""查重：把本仓库的句子和参考语料比对。
用法: python3 tools/dupcheck.py <语料目录或文件...>
语料可以是 html / md 文件。输出完全重复的句子，以及 >=N 字连续重合片段。"""
import re, sys, os, glob, html
N = 18
def norm(s):
    s = re.sub(r'<script.*?</script>|<style.*?</style>', ' ', s, flags=re.S)
    s = re.sub(r'<[^>]+>', ' ', s); s = html.unescape(s)
    s = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', s)
    s = re.sub(r'https?://\S+', '', s)
    return re.sub(r'[\s\W_]+', '', s)
def files(args):
    for a in args:
        if os.path.isdir(a):
            for f in glob.glob(a + '/**/*', recursive=True):
                if os.path.isfile(f): yield f
        else: yield a
corpus = ''.join(norm(open(f, errors='ignore').read()) + '|' for f in files(sys.argv[1:]))
grams = set(corpus[i:i+N] for i in range(len(corpus)-N+1))
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
mine = [f for f in glob.glob(root + '/**/*.md', recursive=True) if '/tools/' not in f and 'UPDATE-HOWTO' not in f]
exact = frag = 0
for f in mine:
    t = re.sub(r'^---.*?---', '', open(f).read(), flags=re.S)
    t = re.sub(r'\(https?://[^)]*\)|\([^)]*\.md\)', '', t)
    for s in re.split(r'[。！？；\n|]', t):
        n = norm(s)
        if len(n) < 10: continue
        if n in corpus:
            exact += 1; print('EXACT', os.path.basename(f), s.strip()[:80])
        else:
            hits = [n[i:i+N] for i in range(len(n)-N+1) if n[i:i+N] in grams]
            if hits: frag += 1; print('FRAG ', os.path.basename(f), hits[0], '<-', s.strip()[:60])
print(f'files={len(mine)} exact_sentence_repeats={exact} fragments>={N}chars={frag}')
