TCP and UDP are both transport-layer protocols that sit on top of IP, but they make very different trade-offs. Here's the breakdown:

## TCP (Transmission Control Protocol)

**Connection-oriented and reliable.** TCP establishes a connection before any data is exchanged and guarantees delivery.

- **Handshake:** Sets up a connection with a three-way handshake (SYN -> SYN-ACK -> ACK) before sending data.
- **Reliable delivery:** Every segment is acknowledged. Lost or corrupted segments are retransmitted.
- **Ordered:** Data arrives in the same order it was sent; out-of-order packets are reassembled correctly.
- **Flow & congestion control:** Adjusts sending rate to avoid overwhelming the receiver or the network.
- **Overhead:** Larger headers (20+ bytes) and more round-trips, which adds latency.

**Good for:** web pages (HTTP/HTTPS), email (SMTP/IMAP), file transfers (FTP), SSH -- anything where correctness matters more than speed.

## UDP (User Datagram Protocol)

**Connectionless and "best-effort."** UDP just fires packets (datagrams) at the destination without setting up a connection or tracking them.

- **No handshake:** Send immediately, no connection setup.
- **No guaranteed delivery:** Lost packets are simply lost unless the application handles retransmission itself.
- **No ordering:** Packets may arrive out of order.
- **No flow/congestion control** (built in).
- **Low overhead:** Small 8-byte header and minimal latency.

**Good for:** live video/voice (VoIP), online gaming, DNS lookups, streaming, and other real-time uses where speed matters more than perfect delivery -- a slightly dropped frame beats a stalled one.

## Quick comparison

| Feature | TCP | UDP |
|---|---|---|
| Connection | Connection-oriented | Connectionless |
| Reliability | Guaranteed delivery | Best-effort |
| Ordering | Ordered | Unordered |
| Speed | Slower (more overhead) | Faster (less overhead) |
| Header size | 20+ bytes | 8 bytes |
| Flow/congestion control | Yes | No |
| Typical uses | Web, email, file transfer, SSH | Streaming, gaming, VoIP, DNS |

**Rule of thumb:** Use TCP when you can't afford to lose data and order matters. Use UDP when you can't afford the latency and can tolerate (or handle yourself) occasional loss. Notably, HTTP/3 uses QUIC, which is built on UDP but adds its own reliability layer on top -- a sign that the line between the two can blur when applications take on the work themselves.
