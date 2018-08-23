import sqlite3

DB_FILE = "mvp.db"

db = sqlite3.connect(DB_FILE)

#######################
### For the crawler ###
#######################


class Address:
    def __init__(
        self,
        ip,
        port,
        worker=None,
        worker_start=None,
        worker_stop=None,
        error=None,
        version_payload=None,
        addr_payload=None,
    ):
        self.ip = ip
        self.port = port
        self.worker = worker
        self.worker_start = worker_start
        self.worker_stop = worker_stop
        self.socket = None
        self.error = error
        self.version_payload = version_payload
        self.addr_payload = addr_payload


def create_tables(db):
    db.execute(
        """
        CREATE TABLE addresses (
            ip TEXT,
            port INTEGER,
            worker TEXT,
            worker_start REAL,
            worker_stop REAL,
            version_payload BLOB,
            addr_payload BLOB
        )
    """
    )


def save_address(db, connection):
    db.execute(
        "INSERT INTO addresses VALUES (:ip, :port, :worker, :worker_start, :worker_stop, :version_payload, :addr_payload)",
        connection.__dict__,
    )


def next_address(db):
    cursor = db.cursor()
    cursor.execute(
        """
        SELECT * FROM addresses
        WHERE worker_start IS NULL
    """
    )
    args = cursor.fetchone()
    return Address(*args)


#######################
### For the monitor ###
#######################


def finished_count():
    pass


def total_count():
    pass


def uncontacted_count():
    pass


def failed_count():
    # error non-empty
    pass


def currently_connected():
    # start time + worker non empty, worker_stop empty
    pass


def earliest_start_time():
    pass


################
### Fixtures ###
################

# https://www.adfinis-sygroup.ch/blog/en/testing-with-pytest/#fixtures
# but do it in-memory