---
layout: post
title:  "I hate Microsoft"
---

It’s not a big deal, but I got really pissed off by Microsoft products yesterday.

My wife asked me to compose an internal newsletter email for her. I thought it should be a piece of cake via a html email with a bit css work.

All of the corporation email in her company is based on MS Exchange Server, and all of them use Outlook 2007/2010 as email client. Pretty standard configuration for a big company.

The first thing I found is that there’s no way to view/edit html source code directly in outlook. All I could do is editing the html, preview it in IE and then click ‘send webpage content via email’ in the browser. Still fair enough, I think. But the problem is that I need embed some images in the mail and reference those images in the html code via content ID. There’s no way to do that directly in IE. Here is the workflow I expect to work.

1. Compose the html via any editor, preview it in IE with all image reference link to local path. When everything looks right, click ‘send webpage content via email’.
2. In outlook ‘New Mail’ view, attach all the reference images, find their content ID by looking at the message header.
3. Edit the html source inside outlook. Replace all image link to the content IDs. Done!

Soon, I found myself too naive to think I’m able to do step 2) and step 3) in Outlook. After googling for 10 mins, I gave up. First, there’s no way to view the content ID of a attached image. Second, there’s no way to view/edit html source for a html email. Note, you could view html source when receiving a html email, but no way to do the same thing when you compose a new mail. How ridiculously!

Well, I suck it. Microsoft treats all of us as muggles, so we shouldn’t touch any black magic like html source code. Although a bit annoying, it’s not a big problem. I could just resort to do some python coding and send the email via MIME and smtp module.

After a couple of hours, I made the html look perfect in IE. And finished the script to send out an email with all the attached images and content ID thing sorted out. Unfortunately, the testing email looks miserable. First, I need say that in the email, I didn’t do any css trick, all I use is common css attributes such as height, width, float, margin etc. At this point, I have to resort to mighty Google again. It turns out that Microsoft switched email html render engine from IE to Word from Outlook 2007. Jesus, what the hell Microsoft is thinking ? IE is horrible enough, and now they’re making it much worse. Word doesn’t follow any CSS standard. Quote from www.campaignmonitor.com, a famous website focused on email campaign, “Microsoft takes email design back 5 years” after releasing Outlook 2007. Email designers now have to use old-school table way to compose a html email thanks to Microsoft. And there’re blog posts about outlook emails hacks all over the internet. To use a background image in email, you have to hack via injecting VML into html. VML, huh, is that thing dead for ten years?!

Due to this Word HTML engine thing, all my work in the previous hours was in vain. I’ve restarted using VML, table/tr/td and white-spacer images. Oh god, I’m finding myself back to college. The tragedy didn’t end at this point. Now I realized that outlook is based on word html engine, so I wrote the html code manually and then open it in word to preview. After 5 minutes, I found out the factor that despite of using the same engine, outlook and word still outputs DIFFERENT RENDERING RESULT for the same html source code! What the F**K! I can’t believe I’ve been wasting time on this damn thing for nearly half a day!

At the end of the day, I just felt really sorry for myself and for those email designers who have to bare with the giant’s stupid move. And now besides Internet Explorer, I have another reason to hate Microsoft.
