---
title: "Your Semi Annual Reminder That MCprep Needs You"
date: 2025-06-29
toc: false
images:
tags:
  - MCprep
---

As we close in on getting the next MCprep update ready
for release, I think it's a good time to add to my
growing collection[^1] [^2] of posts where I try to get
more involvement in MCprep development. By involvement, I
mostly mean the following:

[^1]: See [Problems of MCprep Development](/posts/2023/03/problems-of-mcprep-development/)
[^2]: Also see [MCprep isn't Sustainable](/posts/2023/06/mcprep-isnt-sustaintable/)

- Bug reports
- Assets
- Translations (new one since the last time I've talked about this issue)
- Code

Bug reports are (thankfully) filed more often these days,
and with a lot more detail (though after we moved to the forms
format on GitHub), so there's not really much for me to say
other than "please file more when you get an issue with MCprep".

Assets are, well still very little submissions. To be fair, we do
have a preference towards using 2.8 (and now 2.83) for rig submissions 
for backwards compatibility reasons, but there really hasn't been many 
submissions for rigs/assets so far. This is one area that we leave up to
the community, and unfortunately, we don't get much involement in this
area. For those interested, [here's what we're looking for](https://github.com/Moo-Ack-Productions/MCprep/blob/master/docs/asset_standards.md)
in rig submissions; a great place to get started would be creating
replacements for BSS rigs.

Like assets, translations are also another thing we leave up to the
community. This is a more recent addition, and we do have 2 translations
already in MCprep (Simplified Chinese and Russian). Translation is not
really easy, and we do require all translations to be reviewed for quality
reasons, so I'm not too surprised we don't get much involvement in this
area. For those interested in translation, [you can check out the docs](https://github.com/Moo-Ack-Productions/MCprep/blob/master/docs/i18n/translating.md)
for more info.

And finally, code. Code is something that, while we really do wish we had
more community involvement with, we also understand why it's not common.
However, I do think it's important to at least give some stats and figures
for the MCprep codebase.

Running `sloccount` on MCprep yields us the following:
```
(Data up till commit f8fafd8cb30e97c5a65e75f55bf2df53b9abe323)

Total Physical Source Lines of Code (SLOC)                = 16,837
Development Effort Estimate, Person-Years (Person-Months) = 3.88 (46.54)
 (Basic COCOMO model, Person-Months = 2.4 * (KSLOC**1.05))
Schedule Estimate, Years (Months)                         = 0.90 (10.76)
 (Basic COCOMO model, Months = 2.5 * (person-months**0.38))
Estimated Average Number of Developers (Effort/Schedule)  = 4.33
Total Estimated Cost to Develop                           = $ 523,865
 (average salary = $56,286/year, overhead = 2.40).
```

As of June 2025, MCprep is 16,837 lines of Python (and yes, this is *only*
counting the Python code), and assuming a salary of around 56,000 USD[^3]
would have "costed" around 523,860 USD (rounding the numbers here). Of course,
this stat assumes we were paid to work on MCprep, which we aren't, as MCprep
is completely free software under the GNU GPL[^4].

[^3]: Which as far as I can tell is based on 2004 stats
[^4]: And BSD 3-Clause for CommonMCOBJ parsing

And speaking of "us", we also can't forget stats broken down by dev.

{{< image src="featured.webp" alt="GitHub Insights page breaking down commits by contributor" position="center" style="border-radius: 8px;" >}}

For context, the MCprep dev team (i.e. those who can review and merge pull requsts)
consists of:

- TheDuckCow (who has been working on MCprep for almost *12 years* now)
- zNight
- And of course, myself

Y'all might notice that there's a bit of a recent falloff in the stats for us three,
and that's for a couple of reasons. These include new projects (such as TheDuckCow's
game [Wheel Steal](https://www.wheelstealgame.com/), as well as the road generation
plugin that powers it), work on other open source projects (zNight for example has
done a lot of recent work for [Bforartists](https://www.bforartists.de/), which funnily
enough I'm also a part of for packaging the Flatpak), and life changes (such as myself
entering university). Of course, there's also the aspect that, [until Blender 5.0](https://github.com/Moo-Ack-Productions/MCprep/issues/668)
entered alpha recently, MCprep didn't really break as much in the last year with new
releases. Sure, that doesn't mean we completely forgot about MCprep and adding features[^5],
but new features additions have slowed down in MCprep.

[^5]: See [#600](https://github.com/Moo-Ack-Productions/MCprep/pull/600), [#656](https://github.com/Moo-Ack-Productions/MCprep/pull/656)

For those intersted in contributing to MCprep, [we have written a basic guide](https://github.com/Moo-Ack-Productions/MCprep/blob/master/CONTRIBUTING.md)
on contributing to MCprep. If you need some ideas for what to contribute, [we also have
a few GitHub issues](https://github.com/Moo-Ack-Productions/MCprep/issues?q=sort%3Aupdated-desc+is%3Aopen+label%3A%22first+good+contribution%22)
marked as `First good contribution`, i.e. bugs and features that would make good first contributions
to MCprep. A lot of these are bugs, but there's also some features in there, like 
[#264](https://github.com/Moo-Ack-Productions/MCprep/issues/264) and [#268](https://github.com/Moo-Ack-Productions/MCprep/issues/268).

So get out there and start getting involved :D
