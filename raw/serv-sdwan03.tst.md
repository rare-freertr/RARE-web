# Example: sdwan with fixed addresses
    
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
    logging file debug ../binTmp/zzz75r1-log.run
    !
    crypto rsakey rsa import $v10$TUlJRW93SUJBQUtDQVFFQWdKNDM3SWFwaEc1V0NRN3d0UURhdzFJK1N3ZFU4MFA5RXhPNHRCN3hiRTJXQ0I0U3h1NVZscm1pWG5rVXFHMkc5OVZoVEIrSjFIRkl0ZEttWHRQKzlwOTBwRlpNWFh6YTJjN3F3dUVCUVVxQWdxcVRwZmM1SlZNSVF6UnF2T2pEL1RVNDl6aUJaOGlBVG1mNDcrKys5VHRkRXk0Z1B1SmZVZDhONm1wQXRER0tvVHlYSG5WdzdXNmNiMHR2TnpKTmFsU0xNbUtQOVRxQ1RhQVNPdkN6UEtkVkd1R09ZTzN1T0pvQmtWUlVyb2lKUlRLTXFmTVRiVUNmb1JCb0c3eFpGdW1DZ2ZKcG5iSnRZSzNZb1IvU29LSWRJTjhSMUNUcTJtZnlXdnZZMU12UnlObFpRYWMrdmtCQTdkTzQrQnIxVStWb3lPdjFLWnRuT2dIU243ZWI2UUlEQVFBQkFvSUJBRUNDR241eEUvaXQ5a3pZeDNXaEZoZTgyaTE3WWVvWkFZZGQ3dGU0WlZIeW4vczJTaWlvUlJreHhmUW9PbW8zZE9nOGgyNU1xeTU0R3dYR3YxYjBjUDUwLzJXbE91dnd3VHRaQW5uM3JFOTQ5SGVVNGpUdGlDWG1QVkNucTVsUURXeWtFd3c3dFB1K25rdTA3akE1U01kcW5NWVA3bkJielg4Y3ByZ1p6cFlSUk8vVVBDdTBFMWxIZGJaSXdMUVBNRVpablJkS2V5WkVyaEtnWEFEVVF4WUJjcjF5WXlBd2dCeEpGeExHSUwxdHU2Z2tBanEyMkl3bUF2dGl2V1FIalAyRi9yd05GTEZkQ1JZcTZZbys0NXNXcll6TGNiSktmU2FSNGgyTkJFemI0VVIxYTVTbGxSVkREK0pGbHo2VDZEWXJBQnBodW8yVk5PWGU3aHNtdCtFQ2dZRUF1THVyWnFDdW42bVBZV1hHWjFnRExxQkJlY0dvZ2hrUjhNU3BkanM3VFBibHVHRDNpa09mVmhRdWVWRzFSWFMyamtDODdzLzBZMGgvQ1Q0V0JyNjZyVTRBcVNteDJaU2NxeUVRekpYMjk0b3FYU01nN2piWFpWT2UxTjd2RlVUZFhsU2YrOTdkLzFidU04aHArK2t0UFlFZ0VUSEgxRStTZVVmKytISTZzYVVDZ1lFQXNqeVpmZUE3M2VNYXVhVWtGeVZqWkhkNUhUMkR1RWJiNGZaQ3BpVSs5Tk9mZm14Rm9mWmVYdmhvTkM3aC90dS8veTFscWRNQ0d1V3l0L2xyRGdYaE41dFhNT1pqcXBNTVhOWUZNYUxqRnZySlBjYVFIMDFFN1gzU01PRzVlanFlRTBBMWNHOTQwQXBmMCtCaHpGcG5SV0hRN2RDcW44NCt6ZzFGZVNLbjVmVUNnWUFpTSswS05WbmZpZDlZSXlYVzRIN0dWVG1LTjRiaGY0N0l5MENzK1U2RGMzc1k1aXN1MkZKWjk2YWJJN3V5UG1mR2Nzb0lWVXhrVFhubjFpengxc0p0Yi9IRFlFcmpoQloxd011QmRZcWlUbHlGbmdsczBZNlQzaVdjT0NLQUI1NE01eEl2NmhXa1B3NGZYRTN6TERzS0Zpdy93cjNDMjNDOUw4MVBacWJqV1FLQmdRQ2p0M0l0NDFoYU9nOEVVeUpSZUhCUmlrUmZqVzkrUnVnV0tJT1Q1VVpzMEM0Q2pDVngzY0ZWYnNzWWs2L1d6N2NPQjM4SWZOL0VJUlVHVkQzM2hZTVg5c0lpRXAyZHdyQnFYZFFyZ2JraUZIM2hGcEN2aitRdVdaSkdnREJFaTY5RGM0a2ltK0hYQnBCN0ovSHRLV1VPb0FpdlNTcFEyN3RvdlZ3Qkpzb2VPUUtCZ0h5WXpQSXNYQWpxSVpOM0lrdEYzcEVTMTNSS0Rwc25PdWNrUjFUYjBNQmpkeG03NFg2ZGt0MEZqUklJZFFYQ3p2bnV2cXFobm1VNEhNQUIyenpXV0pVZ0c1YXhkRUhFK3hOLzlXcnVpTE1RaE5WQ01QRUszQ3NINWZneFlkM3Z6aHNBUmZ0akNjT2x6NEgyS1YyTDh5SThOVjVSRitjTFRFcmlYNlJCT1MxMQ==
    !
    crypto dsakey dsa import $v10$TUlJQnVRSUJBQUtCZ0NIRVhWQXA0aFkybGE3K3Y4QzdBYnNLY3Y1aXFKNVlXckpkcFJ6NXV6RVFTeWl4cUVJRWUzcnpQajZ5cWdXK0ZaZFpNNUZjS1YrMVNBd3g3c3lpRWZORGRpZ3NYeVA2dWtmUXlYUmZCV01PT0tvRGRVWlhSblo0b2RXUE42NU0xUUd1OEN0VmtTUmFMTzJ6NEhBNzFRVnBIcFNqeGR4aGlxYy9JdElNNGFnRkFoVUFnUTN0RG9idmd1QitSV2lVM0NkQUxhazZjWUVDZ1lBWE44cU9zM20vRUp6MGpGMkZqbVVYZjdObUtaYWViYTVxQ0ZpS1d2WUlXQ1B1MzZ1R3FVV3U2ZXN4YjhrZURLcVFqOEhOeWM3SVBrMXhBWVBuaUhaeGlYRlovUnYvUXQ1VU5HQ0tFN1ZyNktLWWZ5R0xIaEZRMEpqc0t3Q1pwNHExako1QmcwUlJxSjBWVjF2ZlFSYkZ1K1NtUjhpVkVxYStaTWp0ZC9nSHVRS0JnQk5aVk9VY2ZtMFpZQ1NnSjhZQStPV0l1S0JwTXVWdlgvcDFocnFhaU9jTjhncmVKZ2EwOFBtMUkyMTdHYVlnMHlEanp5TXlUaXpmZVM4TklXbm1oNjg4bEJhT3R5cVJIZmtublJzSVhlTmJrQVErOThhMW1ROURxRmJQUUY3enEzcVQzcWg1NDY4ZG9QZEFrQmdiUjNTUU5xNmZ1TFV5MTVkZXkwUC90bVU4QWhSSGZpTW9mbElXN2FoM0lHRUluaFRFMDVnOGxBPT0=
    !
    crypto ecdsakey ecdsa import $v10$TUhRQ0FRRUVJQUQ5NnV1R3RHRlZ3MHZtK05CMzRBcEltS051MlZMK2s0VTF0N1lpSkdsUW9BY0dCU3VCQkFBS29VUURRZ0FFRlgrQUhRMjR3aTdWclRKbmhZbFRiY1ZyQzdsRDJBRzI4bEVQdENJd0JzZm01Q2ZJWVhLQVl0VDM2Y1ZWdXlDQnlVOVVrWmxSM0l1RWNLS2pFTkEwL1E9PQ==
    !
    aaa userlist usr
     username u
     username u password $v10$cA==
     username u privilege 14
     exit
    !
    ipv4 pool p4 2.2.2.222 0.0.0.1 3
    !
    ipv6 pool p6 2222::222 ::1 3
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
     ipv4 address 1.1.1.99 255.255.255.255
     ipv6 address 1234::99 ffff:ffff::
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
     no description
     vrf forwarding v1
     ipv4 address 1.1.1.1 255.255.255.252
     ipv6 address 1234:1::1 ffff:ffff::
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet2
     no description
     vrf forwarding v1
     ipv4 address 1.1.1.5 255.255.255.252
     ipv6 address 1234:2::1 ffff:ffff::
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet3
     no description
     vrf forwarding v1
     ipv4 address 1.1.1.9 255.255.255.252
     ipv6 address 1234:3::1 ffff:ffff::
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
    server sdwan v9
     security authentication usr
     security rsakey rsa
     security dsakey dsa
     security ecdsakey ecdsa
     pool4 p4
     pool6 p6
     vrf v1
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
    logging file debug ../binTmp/zzz75r2-log.run
    !
    vrf definition tester
     exit
    !
    vrf definition v1
     rd 1:1
     exit
    !
    interface dialer1
     no description
     encapsulation ppp
     vrf forwarding v1
     ipv4 address 2.2.2.2 255.255.255.255
     ipv6 address 2222::2 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
     no description
     vrf forwarding v1
     ipv4 address 1.1.1.2 255.255.255.252
     ipv6 address 1234:1::2 ffff:ffff::
     no shutdown
     no log-link-change
     exit
    !
    proxy-profile p1
     vrf v1
     source ethernet1
     exit
    !
    vpdn sdw
     interface dialer1
     proxy p1
     target 1234::99
     username u
     password $v10$cA==
     prefer ipv6
     protocol sdwan
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
    ipv4 route v1 0.0.0.0 0.0.0.0 1.1.1.1
    !
    ipv6 route v1 :: :: 1234:1::1
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
    
    **r3:**
    ```
    hostname r3
    buggy
    !
    logging file debug ../binTmp/zzz75r3-log.run
    !
    vrf definition tester
     exit
    !
    vrf definition v1
     rd 1:1
     exit
    !
    interface dialer1
     no description
     encapsulation ppp
     vrf forwarding v1
     ipv4 address 2.2.2.3 255.255.255.255
     ipv6 address 2222::3 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
     no description
     vrf forwarding v1
     ipv4 address 1.1.1.6 255.255.255.252
     ipv6 address 1234:2::2 ffff:ffff::
     no shutdown
     no log-link-change
     exit
    !
    proxy-profile p1
     vrf v1
     source ethernet1
     exit
    !
    vpdn sdw
     interface dialer1
     proxy p1
     target 1234::99
     username u
     password $v10$cA==
     prefer ipv6
     protocol sdwan
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
    ipv4 route v1 0.0.0.0 0.0.0.0 1.1.1.5
    !
    ipv6 route v1 :: :: 1234:2::1
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
    
    **r4:**
    ```
    hostname r4
    buggy
    !
    logging file debug ../binTmp/zzz75r4-log.run
    !
    vrf definition tester
     exit
    !
    vrf definition v1
     rd 1:1
     exit
    !
    interface dialer1
     no description
     encapsulation ppp
     vrf forwarding v1
     ipv4 address 2.2.2.4 255.255.255.255
     ipv6 address 2222::4 ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
     no shutdown
     no log-link-change
     exit
    !
    interface ethernet1
     no description
     vrf forwarding v1
     ipv4 address 1.1.1.10 255.255.255.252
     ipv6 address 1234:3::2 ffff:ffff::
     no shutdown
     no log-link-change
     exit
    !
    proxy-profile p1
     vrf v1
     source ethernet1
     exit
    !
    vpdn sdw
     interface dialer1
     proxy p1
     target 1234::99
     username u
     password $v10$cA==
     calling 1701
     prefer ipv6
     protocol sdwan
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
    ipv4 route v1 0.0.0.0 0.0.0.0 1.1.1.9
    !
    ipv6 route v1 :: :: 1234:3::1
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
