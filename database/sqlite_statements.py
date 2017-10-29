# Discord user
create_player_table = """
CREATE TABLE IF NOT EXISTS players (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    uuid TEXT,
    discriminator TEXT,
    UNIQUE (uuid, discriminator)
);"""

create_event_table = """
CREATE TABLE IF NOT EXISTS event (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    description TEXT,
    format TEXT,
    slots INTEGER,
    available_slots INTEGER
);"""

create_participant_table = """
CREATE TABLE IF NOT EXISTS participants (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    player_id INTEGER,
    event_id TEXT,
    seed INTEGER,
    wins INTEGER,
    loses INTEGER,

    FOREIGN KEY (player_id) REFERENCES player (id)
    FOREIGN KEY (event_id) REFERENCES event (uuid)
);"""

statements = [
    create_player_table,
    create_event_table,
    create_participant_table
]
