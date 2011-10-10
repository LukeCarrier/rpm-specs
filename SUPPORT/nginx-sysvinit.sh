#!/bin/sh
# nginx init script
# Written by Luke Carrier <hey@lukecarrier.me>

# nginx configuration
BIN="/usr/sbin/nginx"
CONF="/etc/nginx/nginx.conf"
LOCK="/var/lock/nginx.lock"
PROG="$(basename $BIN)"

# Source functions and configuration
. /etc/rc.d/init.d/functions
. /etc/sysconfig/network

# Do we have networking enabled?
[ "$NETWORKING" = "no" ] && exit 69

# Get the status of the process
_status() {
    status "$PROG"
}

_status_q() {
    _status >/dev/null 2>&1
}

# Start the server
start() {
    [ -x $BIN  ] || exit 77
    [ -f $CONF ] || exit 74
    echo -n $"Starting $PROG"
    daemon "$BIN" -c "$CONF"
    result=$?
    echo
    [ "$result" = "0" ] && touch "$LOCK"
    return "$result"
}

# Stop the server
stop() {
    echo -n $"Stopping $PROG"
    killproc "$PROG" -QUIT
    result=$?
    [ "$result" = "0" ] && rm -f "$LOCK"
    return "$result"
}

# Restart the server
restart() {
    test_config || return $?
    stop
    sleep 1
    start
}

# Reload the server via an HUP
reload() {
    test_config || return $?
    echo $"Reloading $PROG"
    killproc "$PROG" -HUP
    result=$?
    echo
}

# Test configuration files
#   Note: this is a "best-effort" and does fail to detect some syntax issues.
#   No tests take place on actual values at all.
test_config() {
    "$BIN" -t -c "$CONF"
}

# Do something useful
case "$1" in
    "start")
        _status_q && exit 0
        $1
        ;;
    "stop")
        _status_q || exit 0
        $1
        ;;
    "restart"|"force-reload")
        $1
        ;;
    "reload")
        _status_q || exit 75
        $1
        ;;
    "test-config"|"configtest")
        test_config
        ;;
    "status")
        _status
        ;;
    *)
        echo "Usage: $0 {start|stop|restart|reload|test-config|status}"
        ;;
esac
