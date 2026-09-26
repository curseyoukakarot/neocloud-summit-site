"""Regenerate the speaker grid in index.html from the list below.

Edit S (order = display order), drop headshots in assets/speakers/<slug>.jpg
(square, 400x400), then run:  python3 tools/speakers.py
Cards link to LinkedIn when a handle is set; photo if present, else initials."""
import os, re, html
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LI = 'https://www.linkedin.com/in/'
# slug, name, title, company, linkedin handle (None = not verified yet), tag
S = [
 ('nicola-tan','Nicola Tan','Go-to-Market','AMD','nicolatan','Keynote'),
 ('andy-hock','Andy Hock','Chief Strategy Officer','Cerebras','andyhock',None),
 ('matt-ouellette','Matt Ouellette','Sr. Director, AI Product Management','AMD','matthewouellette',None),
 ('carl-brown','Carl Brown','VP of Sales','Supermicro','carlbrown40',None),
 ('liran-zvibel','Liran Zvibel','CEO','WEKA','liranzvibel',None),
 ('val-bercovici','Val Bercovici','Chief AI Officer','WEKA','valentinbercovici',None),
 ('rajeev-koodli','Rajeev Koodli','SVP','SoftBank / Infrinia','rajeevkoodli',None),
 ('rahul-varshneya','Rahul Varshneya','Managing Director','Morgan Stanley','rahul-varshneya-6635b11a',None),
 ('vladimirs-sazonovs','Vladimirs Sazonovs','Global Infrastructure Funds','Cisco','vsazonov',None),
 ('kevin-cochrane','Kevin Cochrane','CMO','Vultr','kevinvcochrane','Keynote'),
 ('syona-sarma','Syona Sarma','VP of Hardware','DigitalOcean','syona-sarma-7824222',None),
 ('vyoma-gajjar','Vyoma Gajjar','Sr. Principal AI Architect','ServiceNow','vyomagajjar',None),
 ('rob-naidoff','Rob Naidoff','VP Americas, GTM','SambaNova','rob-n-6aa43023',None),
 ('simran-arora','Simran Arora','Principal Research Scientist','Together AI','simran-arora',None),
 ('dean-nelson','Dean Nelson','Chairman, iMasons · CEO, Cato Digital','iMasons','deannelson','Keynote'),
 ('aravind-srikumar','Aravind Srikumar','VP of Marketing','Upscale AI','aravind-srikumar-a6227019','Keynote'),
 ('muneeb-rasool','Muneeb Rasool','Founder &amp; CEO','Tensor Machines','muneebrasool','Keynote'),
 ('victor-kuarsingh','Victor Kuarsingh','Formerly Capital One','ex-Capital One','victorkuarsingh',None),
 ('arzoo-mittal','Arzoo Mittal','Technical Program Manager','TransUnion','arzoomittal',None),
 ('drew-pletcher','Drew Pletcher','Principal Architect','Lightning AI','drew-pletcher-a14907',None),
 ('erik-norden','Erik Norden','Executive, AGI Technology &amp; Strategy','Zyphra','eriknorden',None),
 ('alex-yeh','Alex Yeh','CEO','GMI Cloud','gmi-yeh',None),
 ('craig-gieringer','Craig Gieringer','SVP','Massed Compute','craiggieringer',None),
 ('steven-hou','Steven Hou','Head of Research','Silicon Data','steve-hou-001',None),
 ('carmen-li','Carmen Li','CEO','Compute Exchange','carmenrli',None),
 ('simone-giacomelli','Simone Giacomelli','CEO','Prem AI','simone-giacomelli-a8458197',None),
 ('lamia-youseff','Lamia Youseff','CEO','Jazz Computing','lyouseff',None),
 ('bryan-lubin','Bryan Lubin','Managing Director','Moonshot Energy','bryan-a-lubin-8956b119',None),
 ('forrest-heath','Forrest Heath','Co-founder','Panadina','forrestheath3',None),
 ('tiffany-wilson','Tiffany Wilson','CEO','Remanie.ai','tiffanyjwilson',None),
 ('victor-ghadban','Victor Ghadban','Principal Architect','Qumulus',None,None),   # two same-name AI profiles; unverified
 ('matt-renner','Matt Renner','Chief Commercial Officer','Acasia',None,None),     # no confirmed profile yet
 ('sebastian-spitzer','Sebastian Spitzer','Advisor','IgniteGTM','seba-s',None),
 ('bill-barry','Bill Barry','CEO','IgniteGTM','billnbarry','Host'),
]
IN_ICON = ('<svg class="nc-speaker__in" viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M20.45 20.45h-3.56v-5.57c0-1.33-.02-3.04-1.85-3.04-1.85 0-2.14 1.45-2.14 2.94v5.67H9.35V9h3.41v1.56h.05c.48-.9 1.64-1.85 3.37-1.85 3.6 0 4.27 2.37 4.27 5.46v6.28zM5.34 7.43a2.06 2.06 0 1 1 0-4.13 2.06 2.06 0 0 1 0 4.13zM7.12 20.45H3.56V9h3.56v11.45zM22.22 0H1.77C.79 0 0 .77 0 1.73v20.54C0 23.23.79 24 1.77 24h20.45c.98 0 1.78-.77 1.78-1.73V1.73C24 .77 23.2 0 22.22 0z"/></svg>')

def card(slug, name, title, co, handle, tag):
    photo = os.path.exists(os.path.join(ROOT, 'assets/speakers', slug + '.jpg'))
    initials = ''.join(w[0] for w in html.unescape(name).split()[:2])
    avatar = (f'<img src="assets/speakers/{slug}.jpg" alt="" width="200" height="200" loading="lazy" />'
              if photo else f'<span aria-hidden="true">{initials}</span>')
    tag_html = f'<span class="nc-speaker__tag">{tag}</span>' if tag else ''
    inner = (f'<span class="nc-speaker__avatar">{avatar}</span>'
             f'<span class="nc-speaker__body"><span class="nc-speaker__co mono"><span>{co}</span>{tag_html}</span>'
             f'<h3 class="nc-speaker__name">{name}</h3><span class="nc-speaker__title">{title}</span></span>')
    if handle:
        return (f'        <a class="nc-speaker" href="{LI}{handle}/" target="_blank" rel="noopener">{inner}{IN_ICON}'
                f'<span class="nc-sr">LinkedIn profile, opens in a new tab</span></a>')
    return f'        <article class="nc-speaker">{inner}</article>'

p = os.path.join(ROOT, 'index.html'); s = open(p).read()
grid = '\n'.join(card(*row) for row in S)
s, n = re.subn(r'(<div class="nc-speakers" data-reveal>\n).*?(\n      </div>\n      <p class="nc-foot mono" data-reveal>More speakers)',
               lambda m: m.group(1) + grid + m.group(2), s, count=1, flags=re.S)
assert n == 1
open(p, 'w').write(s)
print('cards:', len(S), '| linked:', sum(1 for r in S if r[4]), '| photos:',
      sum(os.path.exists(os.path.join(ROOT, 'assets/speakers', r[0] + '.jpg')) for r in S))
