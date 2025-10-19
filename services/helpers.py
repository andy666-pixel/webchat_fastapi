def save_and_refresh(session, anything):
    session.add(anything)
    session.commit()
    session.refresh(anything)
