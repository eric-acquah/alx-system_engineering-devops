# Ensure pip ias installed
package { 'python3-pip':
  ensure => 'installed',
}


# Install Flask version 2.1.0

package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
