# Using Puppet to install flask v2.1.0 from pip3

package { 'Flask':
  ensure   => '2.1.0',
  name     => 'flask',
  provider => 'pip3',
}
