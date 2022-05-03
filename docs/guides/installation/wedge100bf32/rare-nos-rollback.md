
# **RARE NOS upgrade latest release on Wedge 100BF-32(X or QS)**

```
FREERTR#tna-list-installed
Generation Current Release Git Tag                    KernelID       Kernel Release            Platform                   Install date
-----------------------------------------------------------------------------------------------------------------------------------------------------------
         1         1eta    release-1eta               Debian11_0     5.10.0-8-amd64            accton_wedge100bf_32x      2022-03-28 18:38:17.382194899 +0200
         2         1theta  release-1eta-35-gfdc60bb   Debian11_0     5.10.0-8-amd64            accton_wedge100bf_32x      2022-03-28 18:42:25.607601811 +0200
         3 *       1theta  release-1eta-55-g5a08a99   Debian11_0     5.10.0-8-amd64            accton_wedge100bf_32x      2022-04-08 09:10:41.588185765 +0200
```

```
FREERTR#tna-list-available
INFO: Checking for release tags of https://bitbucket.software.geant.org/scm/rare/rare-nix.git

Version  Status
-------------------------------------------------------------------
       1 Not installed
```

```
FREERTR#tna-install-latest
child 362701 created on 3
child started
INFO: Fetching origin/master
Initialized empty Git repository in /tmp/tmp.RKK4RS54pi/.git/
remote: Counting objects: 966, done.
remote: Compressing objects: 100% (906/906), done.
remote: Total 966 (delta 545), reused 0 (delta 0)        s
Receiving objects: 100% (966/966), 20.81 MiB | 17.27 MiB/s, done.
Resolving deltas: 100% (545/545), done.
From https://bitbucket.software.geant.org/scm/rare/rare-nix
 * [new branch]      1          -> origin/1
 * [new branch]      1alpha     -> origin/1alpha
 * [new branch]      1beta      -> origin/1beta
 * [new branch]      1delta     -> origin/1delta
 * [new branch]      1epsilon   -> origin/1epsilon
 * [new branch]      1eta       -> origin/1eta
 * [new branch]      1gamma     -> origin/1gamma
 * [new branch]      1theta     -> origin/1theta
 * [new branch]      1zeta      -> origin/1zeta
 * [new branch]      CERN       -> origin/CERN
 * [new branch]      hotfix/jordi-sde_9_5_0_hash_fix -> origin/hotfix/jordi-sde_9_5_0_hash_fix
 * [new branch]      inventec   -> origin/inventec
 * [new branch]      master     -> origin/master
 * [new branch]      nightly    -> origin/nightly
 * [new branch]      release-ng -> origin/release-ng
 * [new tag]         release-1  -> release-1
HEAD is now at e7e281d Amend previous commit to support model operation on any kernel
copying path '/nix/store/biyrng0r6fgvwv4g7rh7p30k70z9zagb-freerouter-jar-22.4.30' from 'http://p4.cache.nix.net.switch.ch'...
copying path '/nix/store/v5l53fy60402r42yi8lam2s50wd7lhms-hook' from 'http://p4.cache.nix.net.switch.ch'...
copying path '/nix/store/h128b1jcvqh3g6l78c1s0jwdmm0wwj1a-openjdk-headless-14.0.2-ga' from 'https://cache.nixos.org'...
building '/nix/store/wsz1cg1p62h810pxi7dh63vvnj4ayvx1-freerouter-java-modules.drv'...
these derivations will be built:
  /nix/store/0ayjlf29hr8b1ll0y2hrfbgyhfswayca-bf_router_GRE-module-wrapper.drv
...
...
building '/nix/store/in3kpaw7kd7ns959fhl0j44dd6xb3nv1-builder.pl.drv'...
copying path '/nix/store/2pky7pxssys77jsn016ldpd1dk8s27c9-freerouter.service' from 'http://p4.cache.nix.net.switch.ch'...
building '/nix/store/2pmpkyaa9m30fqy334lznllbq7d17vny-aux-env.drv'...
created 3 symlinks in user environment
building '/nix/store/v9y9nz0lhav0m5faiq44ksmr65ivf9yw-user-environment.drv'...
created 113 symlinks in user environment
INFO: Use "release-manager --switch-to-generation 10" to switch to the new release

process exited with 0 code
```
```
FREERTR#tna-list-installed
Generation Current Release Git Tag                    KernelID       Kernel Release            Platform                   Install date
-----------------------------------------------------------------------------------------------------------------------------------------------------------
         1         1eta    release-1eta               Debian11_0     5.10.0-8-amd64            accton_wedge100bf_32x      2022-03-25 08:40:44.578216971 +0100
         2         1theta  release-1eta-22-gd8500e6   Debian11_0     5.10.0-8-amd64            accton_wedge100bf_32x      2022-03-25 08:48:02.029248582 +0100
         3         1theta  release-1eta-27-g5f056c0   Debian11_0     5.10.0-8-amd64            accton_wedge100bf_32x      2022-03-27 23:57:46.691496126 +0200
         4         1theta  release-1eta-32-g4fb2381   Debian11_0     5.10.0-8-amd64            accton_wedge100bf_32x      2022-03-28 09:51:53.773985464 +0200
         5         1theta  release-1eta-33-ge6051d4   Debian11_0     5.10.0-8-amd64            accton_wedge100bf_32x      2022-03-28 09:55:48.397095140 +0200
         6         1theta  release-1eta-34-gedaf8b2   Debian11_0     5.10.0-8-amd64            accton_wedge100bf_32x      2022-03-28 13:03:28.529174353 +0200
         7         1theta  release-1eta-35-gfdc60bb   Debian11_0     5.10.0-8-amd64            accton_wedge100bf_32x      2022-03-28 13:27:50.621246733 +0200
         8         1theta  release-1eta-57-g176c15e   Debian11_0     5.10.0-8-amd64            accton_wedge100bf_32x      2022-04-09 11:28:20.630407955 +0200
         9 *       1       release-1theta-2-g9070f76  Debian11_0     5.10.0-8-amd64            accton_wedge100bf_32x      2022-04-17 07:40:01.283988320 +0200
        10         2       release-1-4-ge7e281d       Debian11_0     5.10.0-8-amd64            accton_wedge100bf_32x      2022-05-03 11:08:51.218083155 +0200
```

```
FREERTR#tna-switch-to-generation 10
child 363282 created on 3
child started
Set RARE profile generation to 10 and restart freerouter? [y/n] y
process exited with 0 code
Connection closed by foreign host.
...
PAR0001#tna-list-installed
Generation Current Release Git Tag                    KernelID       Kernel Release            Platform                   Install date
-----------------------------------------------------------------------------------------------------------------------------------------------------------
         1         1eta    release-1eta               Debian11_0     5.10.0-8-amd64            accton_wedge100bf_32x      2022-03-25 08:40:44.578216971 +0100
         2         1theta  release-1eta-22-gd8500e6   Debian11_0     5.10.0-8-amd64            accton_wedge100bf_32x      2022-03-25 08:48:02.029248582 +0100
         3         1theta  release-1eta-27-g5f056c0   Debian11_0     5.10.0-8-amd64            accton_wedge100bf_32x      2022-03-27 23:57:46.691496126 +0200
         4         1theta  release-1eta-32-g4fb2381   Debian11_0     5.10.0-8-amd64            accton_wedge100bf_32x      2022-03-28 09:51:53.773985464 +0200
         5         1theta  release-1eta-33-ge6051d4   Debian11_0     5.10.0-8-amd64            accton_wedge100bf_32x      2022-03-28 09:55:48.397095140 +0200
         6         1theta  release-1eta-34-gedaf8b2   Debian11_0     5.10.0-8-amd64            accton_wedge100bf_32x      2022-03-28 13:03:28.529174353 +0200
         7         1theta  release-1eta-35-gfdc60bb   Debian11_0     5.10.0-8-amd64            accton_wedge100bf_32x      2022-03-28 13:27:50.621246733 +0200
         8         1theta  release-1eta-57-g176c15e   Debian11_0     5.10.0-8-amd64            accton_wedge100bf_32x      2022-04-09 11:28:20.630407955 +0200
         9         1       release-1theta-2-g9070f76  Debian11_0     5.10.0-8-amd64            accton_wedge100bf_32x      2022-04-17 07:40:01.283988320 +0200
        10 *       2       release-1-4-ge7e281d       Debian11_0     5.10.0-8-amd64            accton_wedge100bf_32x      2022-05-03 11:08:51.218083155 +0200
```

