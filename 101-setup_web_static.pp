#config

#config
$nginx_conf = "server {
        add_header X-Served-By ${hostname};
        error_page 404 /custom_404.html;
        listen 80 default_server;
        rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4/ permanent;
        listen [::]:80 default_server;

        location /hbnb_static/ {
                alias /data/web_static/current/;
        }


        root /var/www/html;

}"

package { 'nginx':
	ensure => 'present',
	provider => 'apt',
}

file { '/data':
	ensure => 'directory',
}

file { '/data/web_static':
        ensure => 'directory',
}

file { '/data/web_static/releases':
        ensure => 'directory',
}

file { '/data/web_static/releases/test':
        ensure => 'directory',
}

file { '/data/web_static/shared':
        ensure => 'directory',
}

file { '/data/web_static/releases/test/index.html':
        ensure => 'present',
	content => "Holberton School Puppet\n",
}

file { '/data/web_static/current':
        ensure => 'link',
	target => '/data/web_static/releases/test',
}

exec { 'chown -R ubuntu:ubuntu /data/':
	path => '/usr/bin/:/usr/local/bin/:/bin/',
}

file { '/var/www':
        ensure => 'directory',
}

file { '/var/www/html':
        ensure => 'directory',
}

file { '/var/www/html/index.html':
        ensure => 'present',
	content => "Holberton School Nginx\n",
}

file { '/var/www/html/404.html':
        ensure => 'present',
	content => "Ceci n'est pas une page\n",
}

file { '/etc/nginx/sites-available/default':
        ensure => 'present',
	content => $nginx_conf,
}

file { 'nginx restart':
        path => '/etc/init.d/',
}


