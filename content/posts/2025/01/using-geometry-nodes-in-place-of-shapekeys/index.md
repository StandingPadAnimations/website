---
title: "Using Geometry Nodes in Place of Shapekeys"
date: 2025-01-10T00:19:21-06:00
toc: false
images:
tags:
  - Blender
---

Over the past few days I've been experimenting with using
geometry nodes instead of shapekeys for rigs, and for the
most part, I've been able to replace most of the shapekeys
with geometry nodes.

Why geometry nodes? Namely:

- To reduce "magic" in drivers (drivers in my opinion shouldn't
  be required to perform f-curve modifications).
- Non-destructive; shapekeys aren't easy to modify compared to a
  geometry nodes setup.
- More power; geometry nodes simply can do way more then a shapekey,
  especially with modifying attributes.

For example, here's sharp bends implemented in geometry nodes. Sadly
I wasn't able to bring them to the legs (weird issues happened), so
those still use shapekeys.
{{< video src="https://cdn.standingpad.org/2025-01-using-geometry-nodes-in-place-of-shapekeys/arm-sharp-bends.mp4" alt="Showcasing sharp bends using geometry nodes" autoplay="true" loop="true" type="video/mp4" >}}

As for attributes, they make stuff like overriding UV maps much easier.
Why would one want to override UV maps? Well in the case of a Minecraft
rig, slim mode.
{{< video src="https://cdn.standingpad.org/2025-01-using-geometry-nodes-in-place-of-shapekeys/slim-mode.mp4" alt="Slim mode with UV maps automatically handled by geometry nodes" autoplay="true" loop="true" type="video/mp4" >}}

Traditionally this would have required handling the UV maps in the shader,
not to mention issues with solid mode as well. Geometry nodes allows us
to override the UV map, and simplify much of the process.

But perhaps one of the most powerful features of geometry nodes is the
system itself. Specifically the fact that it's just a modifier, and
like all modifiers, it's non-destructive (meaning modifying, changing,
or even disabling is easy).
{{< video src="https://cdn.standingpad.org/2025-01-using-geometry-nodes-in-place-of-shapekeys/fancy-feet.mp4" alt="Non-destructively changing the fancy feet settings of the legs" autoplay="true" loop="true" type="video/mp4" >}}

And like any modifier, it can be reused easily as well. No more having
to manually create a shapekey and manually perform the same change (which
is slightly easier with exact values, but still annoying), just add the
geometry nodes modifier and use whatever node-tree is desired. The main
catch is sometimes meshes may some slight tweaks to work, but that's easy
enough to expose into the modifier itself.

As always, I've uploaded the updated rig on [my resources](/resources) page,
so if you want to look further into the geometry nodes sets, you can do so.

Cya!
