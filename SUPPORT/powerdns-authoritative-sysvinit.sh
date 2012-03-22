#!/bin/sh
#
# powerdns This shell script takes care of starting and stopping powerdns.
#
# chkconfig: 345 80 75
# description: PowerDNS is a versatile high performance \
# authoritative nameserver
# probe: true
# processname: powerdns
# pidfile: /var/run/powerdns/powerdns.pid
# config: /etc/powerdns/pdns.conf

# Source function library.
. /etc/rc.d/init.d/functions

# Source networking configuration.
. /etc/sysconfig/network

# Check that networking is up.
[ "${NETWORKING}" = "no" ] && exit 0

[ -f /usr/sbin/pdns_server ] || exit 0

prefix=/usr
exec_prefix=/usr
BINARYPATH=/usr/bin
SBINARYPATH=/usr/sbin
SOCKETPATH=/var/run/pdns-server

[ -f "$SBINARYPATH/pdns_server" ] || exit 0

[ -r /etc/default/pdns ] && . /etc/default/pdns

cd $SOCKETPATH
suffix=`basename $0 | awk -F- '{print $2}'`
if [ $suffix != "server" ] 
then
	[ -f /etc/powerdns/$suffix/pdns.conf ] || exit 0
	EXTRAOPTS=--config-name=$suffix
	PROGNAME=pdns-$suffix
else
	[ -f /etc/powerdns/pdns.conf ] || exit 0
	PROGNAME=pdns
fi

pdns_server="$SBINARYPATH/pdns_server $EXTRAOPTS"

doPC()
{
	ret=$($BINARYPATH/pdns_control $EXTRAOPTS $1 $2 2> /dev/null)
}


doPC ping
NOTRUNNING=$?

case "$1" in
	status)
		if test "$NOTRUNNING" = "0" 
		then 
			doPC status
			echo $ret
		else
			echo "not running"
		fi 
	;;	

	stop)
		echo -n "Stopping PowerDNS authoritative nameserver: "
		if test "$NOTRUNNING" = "0" 
		then 
			doPC quit
			rm -f /var/lock/subsys/pdns
			echo $ret
		else
			echo "not running"
		fi 
	;;		


	force-stop)
		echo -n "Stopping PowerDNS authoritative nameserver: "
		killall -v -9 pdns_server
		rm -f /var/lock/subsys/pdns
		echo "killed"
	;;

	start)
		echo -n "Starting PowerDNS authoritative nameserver: "
		if test "$NOTRUNNING" = "0" 
		then 
			echo "already running"
		else
			$pdns_server --daemon --guardian=yes
			if test "$?" = "0"
			then
				touch /var/lock/subsys/pdns
				echo "started"	
			fi
		fi 
	;;		

	force-reload | restart)
		echo -n "Restarting PowerDNS authoritative nameserver: "
		echo -n stopping and waiting.. 
		doPC quit
		sleep 3
		echo done
		$0 start
	;;

	reload) 
		echo -n "Reloading PowerDNS authoritative nameserver: "
		if test "$NOTRUNNING" = "0" 
		then 
			doPC cycle
			echo requested reload
		else
			echo not running yet
			$0 start
		fi 
	;;		
		
	monitor)
		if test "$NOTRUNNING" = "0" 
		then 
			echo "already running"
		else
			$pdns_server --daemon=no --guardian=no --control-console --loglevel=9
		fi 
	;;		

	dump)
		if test "$NOTRUNNING" = "0" 
		then 
			doPC list
			echo $ret
		else
			echo "not running"
		fi 
	;;		

	show)
		if [ $# -lt 2 ]
		then
			echo Insufficient parameters
			exit
		fi 
		if test "$NOTRUNNING" = "0" 
		then 
			echo -n "$2="
			doPC show $2 ; echo $ret
		else
			echo "not running"
		fi 
	;;		

	mrtg)
		if [ $# -lt 2 ]
		then
			echo Insufficient parameters
			exit
		fi 
		if test "$NOTRUNNING" = "0" 
		then 
			doPC show $2 ; echo $ret
			if [ "$3x" != "x" ]
			then
				doPC show $3 ; echo $ret
			else
				echo 0
			fi
			doPC uptime ; echo $ret
			echo PowerDNS daemon
		else
			echo "not running"
		fi 
	
	;;		

	cricket)
		if [ $# -lt 2 ]
		then
			echo Insufficient parameters
			exit
		fi 
		if test "$NOTRUNNING" = "0" 
		then 
			doPC show $2 ; echo $ret
		else
			echo "not running"
		fi 
	
	;;		



	*)
	echo pdns [start\|stop\|force-reload\|reload\|restart\|status\|dump\|show\|mrtg\|cricket\|monitor]

	;;
esac
