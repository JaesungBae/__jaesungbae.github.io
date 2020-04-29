import glob,os
wavs = glob.glob('*.wav')
wavs = sorted(wavs)
print(wavs)
for idx, wav in enumerate(wavs):
    cmd = 'mv {} {}'.format(wav, str(idx) + '.wav')
    os.system(cmd)
