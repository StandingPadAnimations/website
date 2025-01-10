---
title: Privacy Policy
showDate: false
showRelatedContent: false
showAuthor: false
showReadingTime: false
showWordCount: false
noComment: true
showPagination: false
---

## Analytics

```txt
Last updated: January 10th, 2025
```

StandingPad.org measures page traffic with a self-hosted instance of [GoatCounter](https://goatcounter.com),
which is [open source](https://github.com/arp242/goatcounter) under a
modified version the [European Union Public License](https://github.com/arp242/goatcounter/blob/master/LICENSE).
[We have a more in-depth privacy policy specifically for analytics](https://stats.standingpad.org/help/privacy)
goes in depth, but here's the gist.

Every unique visitor is considered the same individual for 8 hours. Afterwards,
GoatCounter will consider an individual to be a different person. Cookies are not
used for analytics, only IP addresses (which are hashed when stored to reduce traceability),
and all information is anonymized and can not be traced back to an individual for
GDPR complience (see [here](https://stats.standingpad.org/help/gdpr) for more details).

- None of the information collected can be used to personally identify you
- No information is shared with 3rd parties
- All data is collected from the browser

The following information is collected and retained:

- Visited Page
- Referrers (where the page was visited from)
- Screen size
- Browser, Operating system, Device (desktop, mobile, etc), and screen size
- Country and language

### Goatcounter Instance Information

The self-hosted instance of Goatcounter is ran with binaries directly from upstream,
on a cloud server from [Hetzner](https://www.hetzner.com/), located in one of their
US datacenters. The sha256 checksum and version of the Goatcounter binary as of writing
is the following:

```bash
$ sha256sum ~/bin/goatcounter
21b4c09fa5050f4887781386b35daa8dda487cc83d427951bcd3db3225ac3656 ~/bin/goatcounter

$ ~/bin/goatcounter version
version=v2.5.0; go=go1.21.5; GOOS=linux; GOARCH=amd64; race=false; cgo=true
```
