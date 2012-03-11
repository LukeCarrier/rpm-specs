RPMs!
=====

I got a little bit tired of always compiling stuff for use on the million and
one servers I seem to deploy applications on. I also got tired of keeping all of
this wonderful software up to date. I guess that's why I finally got into the
whole packaging thing.

Here be dragons!
----------------

Well, not quite, but you should be aware of a few things:

* I'm not best maintainer in the world. I'll probably screw up a few things from
  time to time, so please don't hate me. I'll try my best; promise.

* I don't have a repository up yet. I plan on releasing these via CloudFlux, but
  I haven't thought too much into how this will work. I'll write some lovely
  code to automate this another day.

* These packages use all the default configuration. It's probably not ideal. If
  you need a feature I don't compile in or you notice that certain packages
  don't build or install without a little help, drop me an issue or, if you're
  totally awesome, a pull request. If you're feeling detective-ish, you can even
  email me. I will _always_ respond.

* If stuff catches fire, breaks, grows wings and flies away or whatever, I can't
  (and won't) be held liable. I'm only trying to help people. Besides, only
  stupid people blindly install packages on their systems without checking them,
  right?

Erm, what do I do with this?
----------------------------

You build packages! No environment changes should be necessary any more, since
I've gradually phased them all out in favour of sensible defaults ;)

Building packages
-----------------

Although you can install SRPMS (source RPMs that contain the spec file and
pretty much nothing else) directly to your system and build that way, I don't
like doing so. I recommend you build the RPMs directly from the spec files.
Unless you know the command to build the SRPMs, you probably don't need to use
them. (Hint: it's on the RPM man page.)

To have dependency packages and source code managed for you (easier) when you
want to generate an RPM from a spec file, you'll want to do something like:

    cd ~/rpmbuild
    SUPPORT/auto-build.sh SPECS/some-package-version.spec

Alternatively, if you'd rather manage dependencies and sources yourself, the
recommended method is something like:

    cd ~/rpmbuild/SPECS
    rpmbuild -vv -ba some-package-version.spec

Hopefully, the package will build as it should and you'll end up with a working
package you can install like so:

    rpm -i ../RPMS/$(arch)/some-package-version.rpm

And, if it sucks, remove like so:

    rpm -e some-package

If it sucks or fails to build, please do open an issue and let me know why. I
like making things easier, not more difficult.

Enjoy!
------

;D
