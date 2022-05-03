# ** RARE NOS experimental software installation**

This command will install latest commit from [freeRtr](https://github.com/rare-freertr/freeRtr) `master` branch

!!! Tip
    This command is particularly suitable for lab or development environment where it is necessary for testing purpose, to install latest commit from [freeRtr](https://github.com/rare-freertr/freeRtr) `master` branch.


## Experimental software install

``` linenums="0"
FREERTR#tna-install-experimental
child 369223 created on 3
child started
INFO: Installing the latest commit of freertr (7730f95d261c1b3c6ffd29698ad5bf722a578b40) on top of the latest RARE development version
WARNING: this could lead to a failed build or a non-functional application

INFO: Fetching 7730f95d261c1b3c6ffd29698ad5bf722a578b40 from https://github.com/rare-freertr/freeRtr
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0
100 2246k    0 2246k    0     0  2308k      0 --:--:-- --:--:-- --:--:-- 5656k
INFO: Fetching origin/master from https://bitbucket.software.geant.org/scm/rare/rare-nix.git
Initialized empty Git repository in /tmp/tmp.dVOIcyH9Xn/.git/
remote: Counting objects: 970, done.
remote: Compressing objects: 100% (910/910), done.
remote: Total 970 (delta 547), reused 0 (delta 0)
Receiving objects: 100% (970/970), 20.81 MiB | 31.39 MiB/s, done.
Resolving deltas: 100% (547/547), done.
From https://bitbucket.software.geant.org/scm/rare/rare-nix
 * [new branch]      1          -> origin/1
 * [new branch]      CERN       -> origin/CERN
 * [new branch]      inventec   -> origin/inventec
 * [new branch]      master     -> origin/master
 * [new branch]      nightly    -> origin/nightly
 * [new branch]      release-ng -> origin/release-ng
 * [new tag]         release-1  -> release-1
HEAD is now at 2bfa4f4 Make freerouter service less Debian-dependent
copying path '/nix/store/v5l53fy60402r42yi8lam2s50wd7lhms-hook' from 'http://p4.cache.nix.net.switch.ch'...
copying path '/nix/store/f95jkch26wxmqd076bcm976qrn7ml46i-stdenv-linux' from 'https://cache.nixos.org'...
copying path '/nix/store/h128b1jcvqh3g6l78c1s0jwdmm0wwj1a-openjdk-headless-14.0.2-ga' from 'https://cache.nixos.org'...
copying path '/nix/store/9y454xgn2s4x2gkirxba034sv9draci5-zip-3.0' from 'https://cache.nixos.org'...
building '/nix/store/38ivdpkymwb2080y8rmlfyndsfv9jrqc-freerouter-jar-experimental.drv'...
unpacking sources
unpacking source archive /nix/store/iv8h1xjykdl45868grgl0w0b6kbkjiin-tmp.MmBRW6czdM
source root is tmp.MmBRW6czdM
patching sources
configuring
no configure script, doing nothing
building
/build/tmp.MmBRW6czdM/src /build/tmp.MmBRW6czdM
compiling
warning: [options] system modules path not set in conjunction with -source 11
1 warning
packing
/build/tmp.MmBRW6czdM
installing
post-installation fixup
shrinking RPATHs of ELF executables and libraries in /nix/store/rw3nm56z0fk6q4fqw9b1imqvpwg5y6w6-freerouter-jar-experimental
strip is /nix/store/b10shv9yqbgps47y0n8x7l7bq8fmp1i6-binutils-2.31.1/bin/strip
patching script interpreter paths in /nix/store/rw3nm56z0fk6q4fqw9b1imqvpwg5y6w6-freerouter-jar-experimental
checking for references to /build/ in /nix/store/rw3nm56z0fk6q4fqw9b1imqvpwg5y6w6-freerouter-jar-experimental...
building '/nix/store/kdxrw8z02h1kk8cfbqb1y4p8wrqin9lw-freerouter-java-modules.drv'...
these derivations will be built:
  /nix/store/q6f7yzmc009idn54rcgvfz79fmlbpqkc-freerouter-experimental.drv
  /nix/store/ymmh46xnarix2qqwkjflypw5r458bnal-unit-freerouter.service.drv
  /nix/store/05m1lrvqmv8901pws2iama0g2d84g1zx-freerouter.service.drv
these paths will be fetched (0.00 MiB download, 0.01 MiB unpacked):
  /nix/store/d868fmvgpz2bdmfdq02il1flsr1bngs7-hook
  /nix/store/rrfvfy731gzz0qfglmmp6qmnxhsk6w95-hook
copying path '/nix/store/rrfvfy731gzz0qfglmmp6qmnxhsk6w95-hook' from 'https://cache.nixos.org'...
copying path '/nix/store/d868fmvgpz2bdmfdq02il1flsr1bngs7-hook' from 'https://cache.nixos.org'...
building '/nix/store/q6f7yzmc009idn54rcgvfz79fmlbpqkc-freerouter-experimental.drv'...
installing
building '/nix/store/ymmh46xnarix2qqwkjflypw5r458bnal-unit-freerouter.service.drv'...
building '/nix/store/05m1lrvqmv8901pws2iama0g2d84g1zx-freerouter.service.drv'...
building '/nix/store/h1c98g6rfffccb0wiy78ngxx71gvlnxa-user-environment.drv'...
created 113 symlinks in user environment
INFO: Use "release-manager --switch-to-generation 12" to switch to the new release

process exited with 0 code
```

## Local installation check

``` linenums="0"
FREERTR#tna-list-long-installed
Generation Current Release Git Tag                    KernelID       Kernel Release            Platform                   Install date
-----------------------------------------------------------------------------------------------------------------------------------------------------------
         1         1eta    release-1eta               Debian11_0     5.10.0-8-amd64            accton_wedge100bf_32x      2022-03-25 08:40:44.578216971 +0100
         2         1theta  release-1eta-22-gd8500e6   Debian11_0     5.10.0-8-amd64            accton_wedge100bf_32x      2022-03-25 08:48:02.029248582 +0100
         3         1theta  release-1eta-27-g5f056c0   Debian11_0     5.10.0-8-amd64            accton_wedge100bf_32x      2022-03-27 23:57:46.691496126 +0200
         4         1theta  release-1eta-32-g4fb2381   Debian11_0     5.10.0-8-amd64            accton_wedge100bf_32x      2022-03-28 09:51:53.773985464 +0200
         5         1theta  release-1eta-33-ge6051d4   Debian11_0     5.10.0-8-amd64            accton_wedge100bf_32x      2022-03-28 09:55:48.397095140 +0200
         7         1theta  release-1eta-35-gfdc60bb   Debian11_0     5.10.0-8-amd64            accton_wedge100bf_32x      2022-03-28 13:27:50.621246733 +0200
         8         1theta  release-1eta-57-g176c15e   Debian11_0     5.10.0-8-amd64            accton_wedge100bf_32x      2022-04-09 11:28:20.630407955 +0200
         9         1       release-1theta-2-g9070f76  Debian11_0     5.10.0-8-amd64            accton_wedge100bf_32x      2022-04-17 07:40:01.283988320 +0200
        10         2       release-1-4-ge7e281d       Debian11_0     5.10.0-8-amd64            accton_wedge100bf_32x      2022-05-03 11:08:51.218083155 +0200
        11 *       1       release-1                  Debian11_0     5.10.0-8-amd64            accton_wedge100bf_32x      2022-05-03 12:39:00.163811926 +0200
        12         2       release-1-5-g2bfa4f4-freertr-7730f9 Debian11_0     5.10.0-8-amd64            accton_wedge100bf_32x      2022-05-03 15:26:08.879322614 +0200
```


!!! Tip
    A new generation `12` has been created and has a special name encompassing RARE-NIX and freeRtr short commit (respectively `g2bfa4f4` and `7730f9`)


## Switch to new software release

``` linenums="0"
FREERTR#tna-switch-to-generation 12
child 371503 created on 3
child started
Set RARE profile generation to 12 and restart freerouter? [y/n] y
process exited with 0 code
Connection closed by foreign host.
```

Check software locally installed

``` linenums="0"
FREERTR#tna-list-installed
Generation Current Release Git Tag                    KernelID       Kernel Release            Platform                   Install date
-----------------------------------------------------------------------------------------------------------------------------------------------------------
         1         1eta    release-1eta               Debian11_0     5.10.0-8-amd64            accton_wedge100bf_32x      2022-03-25 08:40:44.578216971 +0100
         2         1theta  release-1eta-22-gd8500e6   Debian11_0     5.10.0-8-amd64            accton_wedge100bf_32x      2022-03-25 08:48:02.029248582 +0100
         3         1theta  release-1eta-27-g5f056c0   Debian11_0     5.10.0-8-amd64            accton_wedge100bf_32x      2022-03-27 23:57:46.691496126 +0200
         4         1theta  release-1eta-32-g4fb2381   Debian11_0     5.10.0-8-amd64            accton_wedge100bf_32x      2022-03-28 09:51:53.773985464 +0200
         5         1theta  release-1eta-33-ge6051d4   Debian11_0     5.10.0-8-amd64            accton_wedge100bf_32x      2022-03-28 09:55:48.397095140 +0200
         7         1theta  release-1eta-35-gfdc60bb   Debian11_0     5.10.0-8-amd64            accton_wedge100bf_32x      2022-03-28 13:27:50.621246733 +0200
         8         1theta  release-1eta-57-g176c15e   Debian11_0     5.10.0-8-amd64            accton_wedge100bf_32x      2022-04-09 11:28:20.630407955 +0200
         9         1       release-1theta-2-g9070f76  Debian11_0     5.10.0-8-amd64            accton_wedge100bf_32x      2022-04-17 07:40:01.283988320 +0200
        10         2       release-1-4-ge7e281d       Debian11_0     5.10.0-8-amd64            accton_wedge100bf_32x      2022-05-03 11:08:51.218083155 +0200
        11         1       release-1                  Debian11_0     5.10.0-8-amd64            accton_wedge100bf_32x      2022-05-03 12:39:00.163811926 +0200
        12 *       2       release-1-5-g2bfa4f4-freer Debian11_0     5.10.0-8-amd64            accton_wedge100bf_32x      2022-05-03 15:26:08.879322614 +0200
```

Check freeRtr version in use

``` linenums="0"
FREERTR#show platform
freeRouter v22.5.3-cur, done by cs@nop.

name: FREERTR
hwid: accton_wedge100bf_32x
hwsn: null
uptime: since 2022-05-03 17:51:05, for 00:00:21
reload: code#3=user requested
rwpath: /etc/freertr/
hwcfg: /etc/freertr/rtr-hw.txt
swcfg: /etc/freertr/rtr-sw.txt
cpu: 8*amd64
mem: free=299m, max=2147m, used=351m
host: Linux v5.10.0-8-amd64
java: N/A v14.0.2-internal @ /nix/store/7yx2ng37byikwxf4a2b08aqkjp23r2zc-openjdk-headless-14.0.2-ga-minimal-jre
jspec: Oracle Corporation (Java Platform API Specification) v14
vm: Oracle Corporation (OpenJDK 64-Bit Server VM) v14.0.2-internal+0-adhoc..jdk14u-jdk-14.0.2-ga
vmspec: Oracle Corporation (Java Virtual Machine Specification) v14
class: v58.0 @ /nix/store/rw3nm56z0fk6q4fqw9b1imqvpwg5y6w6-freerouter-jar-experimental/rtr.jar
```
