# TCP vs. UDP

TCP and UDP are the two main transport-layer protocols used to send data over IP networks. They differ mainly in whether they guarantee delivery and ordering, and in the overhead that guarantee costs.

## The short version

- **TCP (Transmission Control Protocol)** is connection-oriented and reliable. It guarantees that data arrives complete, in order, and without duplicates — at the cost of more overhead and latency.
- **UDP (User Datagram Protocol)** is connectionless and "fire and forget." It just sends packets (datagrams) with no guarantee they arrive, arrive in order, or arrive only once — but it's lightweight and fast.

## Side-by-side comparison

| Feature | TCP | UDP |
|---|---|---|
| Connection | Connection-oriented (handshake first) | Connectionless (no setup) |
| Reliability | Guaranteed delivery | No guarantee |
| Ordering | Packets reassembled in order | No ordering |
| Error handling | Detection + retransmission | Detection only (drops bad packets) |
| Flow/congestion control | Yes | No |
| Speed / latency | Slower, higher overhead | Faster, lower overhead |
| Header size | 20+ bytes | 8 bytes |
| Data unit | Stream of bytes | Discrete datagrams |
| Broadcast/multicast | No | Yes |

## How they work

**TCP** establishes a connection with a three-way handshake (SYN, SYN-ACK, ACK) before any data flows. It numbers every byte, waits for acknowledgments, retransmits anything lost, and reorders packets that arrive out of sequence. It also adjusts its sending rate to avoid overwhelming the network or receiver (flow and congestion control). The result is a reliable, ordered byte stream — at the cost of round-trips and bookkeeping.

**UDP** simply wraps your data in a small header and sends it. There's no handshake, no acknowledgment, no retransmission, and no built-in ordering. If a packet is lost or arrives out of order, UDP won't fix it — that's left to the application if it cares. This makes UDP leaner and faster, and it's the only one of the two that supports broadcast and multicast (one-to-many delivery).

## When to use which

**Use TCP when correctness matters more than speed:**
- Web pages (HTTP/HTTPS over TCP)
- Email (SMTP, IMAP)
- File transfers (FTP, SFTP)
- Anything where a missing or scrambled byte breaks things

**Use UDP when speed and low latency matter more than perfect delivery:**
- Live video and voice (VoIP, video calls)
- Online gaming
- Live streaming
- DNS lookups
- IoT/telemetry where occasional loss is acceptable

## A useful analogy

TCP is like a phone call: you both say hello, confirm you can hear each other, and acknowledge along the way ("right," "uh-huh"). UDP is like shouting across a room or mailing postcards: the message goes out immediately, but you don't know for sure it landed, and several postcards might arrive out of order — or not at all.

## A nuance worth knowing

"TCP reliable, UDP unreliable" is the right mental model, but UDP isn't unreliable by design flaw — it's deliberately minimal so applications can build exactly the guarantees they need. Modern protocols do this: **QUIC** (the basis of HTTP/3) runs over UDP and re-implements its own reliability and ordering, getting TCP-like guarantees with lower latency and fewer of TCP's limitations.
