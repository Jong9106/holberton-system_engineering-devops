# Fix server number of open files
exec {
  '/usr/bin/env sed -i s/holberton/juan/ /etc/security/limits.conf':
}