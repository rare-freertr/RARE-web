# **RARE NOS release upgrade on Wedge 100BF-32(X or QS)**


```
FREERTR#tna-update-release 1
child 365039 created on 3
child started
INFO: Checking for release tags of https://bitbucket.software.geant.org/scm/rare/rare-nix.git
INFO: Fetching c21fc88ae721207b45081073400d7ddc49fa05b8 from https://bitbucket.software.geant.org/scm/rare/rare-nix.git
Initialized empty Git repository in /tmp/tmp.oMrSEPbvVa/.git/
remote: Counting objects: 970, done.
remote: Compressing objects: 100% (910/910), done.
remote: Total 970 (delta 547), reused 0 (delta 0)
Receiving objects: 100% (970/970), 20.81 MiB | 33.62 MiB/s, done.
Resolving deltas: 100% (547/547), done.
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
HEAD is now at c21fc88 Bump version of bf-sde-nixpkgs to 3434a2
copying path '/nix/store/2i5lj8gcjg68qxl4cglinnkci6wxsjj5-freerouter-jar-22.4.23' from 'http://p4.cache.nix.net.switch.ch'...
building '/nix/store/g5h810qg9xs1dsr67x2ll0hnq44zpnfz-freerouter-java-modules.drv'...
these paths will be fetched (0.00 MiB download, 0.74 MiB unpacked):
  /nix/store/1ix3kvy4v9vr9l31isv750kyq1sgfrr9-freertr-exec-stop-post
  /nix/store/3hhq1il3am1ly12b91ic41idpfywsig1-rtr-hw.txt
  /nix/store/50wh9p15nlqbg3mc7snfhnmzhmi12lw6-release-manager-1
  /nix/store/9g0kd84y36vzg3q6fbhvlgalpchbyi8z-freerouter-native-22.4.23
  /nix/store/m3xbfn478kbkmfr36jw9gbcnazzqp1jc-freerouter.service
  /nix/store/pxarww4k4a66m5dlycabmpqrj527am81-RARE-scripts
  /nix/store/rs3l4jpil434n9zsc6cqn9rcfjw8s8pn-freertr-switch-gen
  /nix/store/zr8vx2nj0yv1nn2qvhxa4sd3yynvby1b-freerouter-22.4.23
copying path '/nix/store/zr8vx2nj0yv1nn2qvhxa4sd3yynvby1b-freerouter-22.4.23' from 'http://p4.cache.nix.net.switch.ch'...
copying path '/nix/store/9g0kd84y36vzg3q6fbhvlgalpchbyi8z-freerouter-native-22.4.23' from 'http://p4.cache.nix.net.switch.ch'...
copying path '/nix/store/50wh9p15nlqbg3mc7snfhnmzhmi12lw6-release-manager-1' from 'http://p4.cache.nix.net.switch.ch'...
copying path '/nix/store/pxarww4k4a66m5dlycabmpqrj527am81-RARE-scripts' from 'http://p4.cache.nix.net.switch.ch'...
copying path '/nix/store/rs3l4jpil434n9zsc6cqn9rcfjw8s8pn-freertr-switch-gen' from 'http://p4.cache.nix.net.switch.ch'...
copying path '/nix/store/3hhq1il3am1ly12b91ic41idpfywsig1-rtr-hw.txt' from 'http://p4.cache.nix.net.switch.ch'...
copying path '/nix/store/1ix3kvy4v9vr9l31isv750kyq1sgfrr9-freertr-exec-stop-post' from 'http://p4.cache.nix.net.switch.ch'...
copying path '/nix/store/m3xbfn478kbkmfr36jw9gbcnazzqp1jc-freerouter.service' from 'http://p4.cache.nix.net.switch.ch'...
building '/nix/store/b64rmp9k7qpd7xqdbsfimarn2yrrp022-user-environment.drv'...
created 113 symlinks in user environment
INFO: Use "release-manager --switch-to-generation 11" to switch to the new release

process exited with 0 code
```

```
FREERTR#tna-update-release 11
child 366116 created on 3
child started
INFO: Checking for release tags of https://bitbucket.software.geant.org/scm/rare/rare-nix.git
ERROR: Release 11 does not exist

process exited with 65280 code
% returned 255
```

!!! Tip
    Once the release has been upgradeed, do not forget to switch the new generation. Here:
    `tna-switch-to-generation 11`


