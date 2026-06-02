Both are ways computers send data over a network, but they make opposite trade-offs.

**TCP (Transmission Control Protocol) — reliable, ordered.**
- Sets up a connection first (a "handshake") before sending.
- Guarantees delivery: if a piece goes missing, it's re-sent.
- Keeps everything in order.
- Trade-off: that bookkeeping adds a little overhead and delay.
- Used when correctness matters: web pages, email, file downloads.

**UDP (User Datagram Protocol) — fast, no guarantees.**
- No handshake — just fires packets off ("fire and forget").
- No re-sending and no ordering; some packets may arrive late, out of order, or not at all.
- Trade-off: much less overhead, so it's faster and lower-latency.
- Used when speed beats perfection: live video/voice calls, gaming, streaming.

**Analogy:** TCP is a phone call where you both confirm you heard each other; UDP is shouting updates across a room — quick, but a missed word is just gone.

Rule of thumb: need every byte intact → TCP. Need it *now* and can tolerate small losses → UDP. Want a diagram of the TCP handshake?
