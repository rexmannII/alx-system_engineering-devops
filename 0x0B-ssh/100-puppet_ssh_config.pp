#!?usr/bin/env bash
# using Puppet to make changes to our configuration file.
# client configuration file (w/ Puppet)
file {'/etc/ssh/ssh_config':
        ensure	=> 'preset',
}

file_line {'Turn off passwdauth',
        path    => '/etc/ssh/ssh_config',
        line    => 'passwordAuthentication no',
        match   => 'passwordAuthentication yes',
        replace => 'true',
}
file_line {'Declare identity file':
        path    => '/etc/ssh/ssh_config',
        line    => 'IdentityFile ~/.ssh/school',
        match   => '^IdentityFile',
        ensure  => 'present',

