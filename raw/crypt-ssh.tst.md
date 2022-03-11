# Example: ssh test
    
=== "Topology"
    
     <div class="nextWrapper">
         <iframe src="/guides/reference/snippets/next-diagram.html" style="border:none;"></iframe>
     </div>

    
=== "Configuration"
    
    **r1:**
    ```
    hostname r1
    buggy
    !
    logging file debug ../binTmp/zzz43r1-log.run
    !
    crypto rsakey rsa import $v10$TUlJRXBBSUJBQUtDQVFFQWxObTFpKy9HMnlCbDlMMHFnendtR1NjaTlYWFlkN2xVTGJzdk5UWEdkZ3VCVlJwMzd5a1pXVk0yQ2gyMHhBbzh4WCtDaVJySCtySnVZYVFoN3YwYUR4MStQM1NEb2NLQS9qUXhLZDhDWitCMnRCWGtUWUlMZ29qTnQwb2FHOERBL1Q1TmVKL2RDK2I0UHRXZnJjQktITk4rbjhKdi9EdUJRWCtqL1VxelVkeVg3THFZeTNlT1kvVkRwVHB2OFREa1pPMHdGYkZGMkJIQkJ0b0ZzSUl2cXZEK1RPOXEzQWExMXY0YUhuQ3FkMmg5dlp6Z2JvREN5MTZxMkJkcWE3WFEycU1YYXNXWkRwQ0Y4ajcySHBONkJDVFNxTzR3Z1YveUpxYkI0SkdMd0xXWVNWaVUvMXRGSVN4OUx0THNLUVhYMzZoZ0lXblltSXRpVzJvaTVxK25jUUlEQVFBQkFvSUJBR1Q5cFRoeGtia0FyVXcwd0ZCVUVnRkUxV28yNzR5amVHS2l1cS9lY1cyTDlzNzM2Mkdmdit3a0Vla2hLSkZONU5lVzRNa0hHNkdUU0dNRkNtVHM0cTVZczF4NFFBc1RQWk83YzVQV0UvckloNkU5clMyTlN5UGdqN3FKRTFlN0d2VjNQUGJYZUJGb1B3dmF3c0VQVXZsbDRXYWhkSHR0SUJDQmVwRVRDc0ZCM2N4VWY0aVd2c0ZqQklobktKMk5XL0JReUg1cENMNkVQeWorazBkUG4wUUxNcjA2TGI1cFRkZkdHVVVRcUFKQTBENEExM3dhM0hpTnhjUHE2b0tDamdIa3NxKzFWRjNnWU1mSEJyb0xJOTdGU3VXZXBSNVZkcjBuWE5rcWdsd0pCUEhHZ1YzT0RHTlRSdEUzVmxJUWppZTdFYzFiSTF1NGt6YTY1UHp0QmZFQ2dZRUE2V296UGxyQWZZcEhxbkMwT1VLSndHdVpzNDFjYm42L0l6UVAyZVl5RVc0M3R0MFM0OWVUMmZmeGd3T2EvWUhPNlM0TjkySnFYdU5TZTBpK2FZR0NzMnMvMm1aRTY0VjNpUDl0UVU5YTVDQjNJbEQ5SGJnU1NOcFRQSXVIUGtId1drWTNzU0pXSG0vVVB6RXpIVjJBS3ZtSlIwN2JCTG5qOXF0OXg4S1JPOTBDZ1lFQW8wRE9tR2xweHdBTDI2amh2OWpCcG5YSXVXWGpVcW1DenFsWUhHSmgwQmJLcjBxR2pDazU3RkJVdE5jc3hEVkJDb2VZYWJOemhmekxyenNPYTZvNVNLdU5zMzFmUVkrdUFkamNSaHRpdDl1eExnRHdmOGpNazExcDE0NHc5MG1XZUVFdktXWVF2Vk5ZdVpZZU1nNFE4YkVTYzJaMVlFWlZIckZNZEE5VU9xVUNnWUExdksxdmZaVXpVZEtOK3NTREtqNXNmbGswYlNjS2lVT1g1elIvQmZBZzh5OEFlb1VPejJMS203cU9YeFlmcHZMcjNCNTdCYjFYZXg1U0k3MHlyUTVhSUNiak1RaE04TDFFWFFuYUwxck5pbXZqQ3FJN1pWVlFVSE01VFNZbHZ5aUdvQVBTVkFWZm5IOVF6UkxuZjg4eUZhRDFPY0pTcERsSFlOUGtXWGIyUVFLQmdRQ1lBUGFieU1MWnJIeGVDWEF3N2dUWkZpQlFKOE15cTJ5Rk9mNDFaNUZGYklOS0ZhMFRnaXRSa2paY3IyRWFTNitFdTE0NVJRSlNobCtzaCtOVWNnbW1WVDI2R3dqL2hXVnlpTllJWE9WYzVheWlkZk40TjZIcnNIV2xZOXJKMVhYS0FIK0dIMmVFc0w4VEJlaVZtSzFFTFNoTjFOK0RSZGxwbTVIaEdvakZsUUtCZ1FERXFjeHh3Q3VvUnJEVmw0andNaVcxeGcraW10Y2pNWFRPVGpyNVRxT2JCdVBUcW96bGxieTJ2OUo4THFMeGtOaDA2ODZFeitXK3FhSFZHVnVrRy9hQm9yaHpNWHpnV0RYZG91YjI5UXlGZkNFTS9uL0M3ZVF4TUs4emxrVWF4am1JcUs2T0crc1g3enV0dHM3VVlHU0wwY0tMWXpLQXE1TkQ2R2tuK1dSZ1dnPT0=
    !
    crypto dsakey dsa import $v10$TUlJQnV3SUJBQUtCZ1FDL0x0cEVUYi9HQ1RJcXp1UTFIeG80SVI5Y0Fubml2bEFKUVlKa2ZNcVJLQUxKaTdLWUVHeUMrWnhRV3JuN3ZTdFI3V2J4TFhLZzg4NWZvRFBNOEFKSFVUZFh1cnpidjlIQ205MGZuRDFiNjhqQXMzcGxHbTZKTHRoaThhMVh4WmhKWFJZRDRoZEJNbkNsbFBBdUpMdTFSWDY4bEU3QUw2NFFHQ1hQNlVJcUFRSVZBUEtZd1RQbmkxLzRRbU90TU8zdzFUZkI4N2pyQW9HQU90a2toOTMvMjAzNitvUEpqd0Q2SFNKT2NzRzZBcEdJWHZBNVB5bGJZTm84SlM3YU9ic1Y1R0RlMGVLcmxSWVBNMXFnYkpabWtTVzR3eUpmT0U1N29MRXhXM3pEYnVCZjRKMjZkcjVTYm90T1B0ZTRNOWtMdFpJUjUxYWZJdVdGUVlTY0lMbi9lSm0rRkVaUWdBdm5zcFpEckQ4dGZGenNzc1BVK3ZOd0VYa0NnWUJhR0krOEFSSG1XcWZnNXRPeEYyNkRYbVlNRjZsVjgyT0h5bHlVUExTNTdXUVI0aytSVWRuMTJZV0E2U2trcy9sdldMaUtRVXp1RkhDaUdTUGQwWWdiSFIzaGo3c1VEM0tBRE54WUkvSWMwRmczY28rYTdXemplOWZUMlNQQ0RzMWVISmtTZE1YeFpYM1hTa0w4TXZQRUkwaEVHQW51eVZYZGt0Z0hab2NzamdJVkFLL2VNSXo4WThzUytwVTdoczkrWkdxL1Iydmo=
    !
    crypto ecdsakey ecdsa import $v10$TUhNQ0FRRUVIMk5HZmJLWVk0VFZwUVM4Rkl5V2FycXhSMDhFc0lrelA1V2RMMHZpeWxLZ0J3WUZLNEVFQUFxaFJBTkNBQVFobmNCQWJJZlBSSk9xeTlxM0cxS1NjcDZ4dndtZ28yME9iWk1aY2paZ0w4eWpTQjZCYXplZTVtUXJnU1ZvZE52VDVveGhCZFFBSkZrT29TTmJzcFli
    !
    aaa userlist usr
     username c
     username c password $v10$Yw==
     username c privilege 14
     exit
    !
    vrf definition tester
     exit
    !
    vrf definition v1
     rd 1:1
     exit
    !
    interface loopback0
     no description
     vrf forwarding v1
     ipv4 address 2.2.2.2 255.255.255.255
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
     no description
     vrf forwarding v1
     ipv4 address 1.1.1.1 255.255.255.0
     ipv6 address 1234::1 ffff::
     no shutdown
     no log-link-change
     exit
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    server telnet ssh
     security protocol ssh
     security authentication usr
     security rsakey rsa
     security dsakey dsa
     security ecdsakey ecdsa
     port 666
     no exec authorization
     no login authentication
     vrf v1
     exit
    !
    server telnet tester
     security protocol telnet
     no exec authorization
     no login authentication
     vrf tester
     exit
    !
    !
    end
    ```
    
    **r2:**
    ```
    hostname r2
    buggy
    !
    logging file debug ../binTmp/zzz43r2-log.run
    !
    vrf definition tester
     exit
    !
    vrf definition v1
     rd 1:1
     exit
    !
    interface ethernet1
     no description
     vrf forwarding v1
     ipv4 address 1.1.1.2 255.255.255.0
     ipv6 address 1234::2 ffff::
     no shutdown
     no log-link-change
     exit
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    !
    server telnet tester
     security protocol telnet
     no exec authorization
     no login authentication
     vrf tester
     exit
    !
    !
    end
    ```
