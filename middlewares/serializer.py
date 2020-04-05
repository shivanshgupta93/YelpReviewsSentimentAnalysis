#### converting the data returned from database into a JSON format
def serialize(rows):
    row2dict = lambda r: {c.name: str(getattr(r, c.name)) for c in r.__table__.columns}
    return [row2dict(row) for row in rows]
