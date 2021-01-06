# websphereusergroup

Migrating the old PHP code base from back when dinosaurs roamed the earth to something slightly more modern.

Decided I'd have a go at writing the whole website in Golang, just to see how it compared to my recent experiences with Python/Flask.

---

## To Do

- [ ] Basic web-app written in go, deployed to a sub-domain to get CI up and running
- [x] Identify features of website to retain
- [x] Identify data remodelling to remove need for MySQL
- [ ] Build Home Page
- [ ] Build Vendors panel
- [ ] Build About Page
- [ ] Build Contacts Page
- [ ] Build Meetings Page
- [ ] Build Downloads Page
- [ ] Learn how to test in golang properly
  - [ ] Mocking
  - [ ] Coverage
- [ ] Redirection from old URLs needed? Download links especially I think
- [ ] Check responsiveness
- [ ] Sitespeed optimisations perhaps?
- [ ] Instrumentation into Prometheus

## Feature Enhancement

- [ ] Ads? Contributions?
- [ ] Tracking - probably need to capture privacy implications or get rid of this stuff
- [ ] Bit of a push towards my blog perhaps?
- [ ] Highlight that it is an archive of an old group, no longer maintained

---

## Rebuild

- Home Page
  - Upcoming Events - static content that is easily updated
  - Previous Meeting - looks up most recent from DB and renders
  - What Is: config
  - Notices: config
  - Testimonials: config
  - Reading: config
- Vendors: shown in right-hand nav on most pages but not all
- Header: shown on all pages
- Footer: measures page speed
- About: simple entities in datastore
  - should build something that makes it easy to upsert the data from local store, don't need full editor any more
- Meetings: lists all meetings
  - Meeting page has metadata top and bottom with table rendered in middle
  - **Bin the table view completely and just use the agenda** table is streams/sessions
- Downloads: may as well move to list of Meetings rather than dropdown - old school
  - takes through to page listing all sessions per stream, with presenter and download link
- Contact: move to using my API. Has recaptcha

### Retired Features

- Questionnaires
- Admin section
- News section - just put in config
- Pages - don't need CMS features, just have as routes

### Data Model

- Entity: Meeting
  - id, location, date, info
- Entity: Stream
  - id, meeting, name, colour, order
- Entity: Session
  - id, stream, session_num, title, speaker_ids, abstract, download
- Entity: Speaker
  - id, meeting, name, photo, bio
- Entity: Vendor
  - id, title, image, url, order(?)
