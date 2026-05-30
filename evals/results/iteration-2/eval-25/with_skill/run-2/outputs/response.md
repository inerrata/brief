# How DNS Resolution Works

DNS (Domain Name System) translates human-readable domain names like `example.com` into IP addresses like `93.184.216.34` that computers use to route traffic. Here's how the process works step by step.

---

## The core idea

Your computer doesn't know where `example.com` lives. It needs to ask. DNS is the system of servers it asks — a distributed, hierarchical directory for the internet.

---

## Step-by-step: what happens when you type a URL

**1. Browser cache check**
Your browser first checks if it already has the IP address cached from a recent visit. If yes, it skips the lookup entirely.

**2. Operating system cache check**
If the browser doesn't have it, it asks the OS. The OS checks its own DNS cache and the local `hosts` file.

**3. Recursive resolver (your ISP or DNS provider)**
If no cache hit, your computer sends a query to a recursive resolver — typically provided by your ISP, or a public one like Google's 8.8.8.8 or Cloudflare's 1.1.1.1. This resolver does the heavy lifting on your behalf.

**4. Root nameserver**
The recursive resolver asks a root nameserver: "Where do I find `.com` domains?" There are 13 sets of root nameservers worldwide. The root server responds with the address of the TLD nameserver for `.com`.

**5. TLD (Top-Level Domain) nameserver**
The resolver asks the `.com` TLD nameserver: "Where do I find `example.com`?" It responds with the address of the authoritative nameserver for that specific domain.

**6. Authoritative nameserver**
The resolver asks the authoritative nameserver — the server the domain owner has configured (usually managed by their registrar or DNS provider): "What's the IP for `example.com`?" It returns the actual IP address.

**7. Response travels back**
The recursive resolver returns the IP to your computer. Your browser now has the address and connects to the web server.

**8. Caching**
Each answer comes with a TTL (Time to Live) value — how long the result should be cached before re-querying. Common values range from a few minutes to 24–48 hours.

---

## The hierarchy at a glance

```
Root (.)
  └── TLD (.com, .org, .net, .io, etc.)
        └── Authoritative nameserver (example.com)
              └── Individual records (A, CNAME, MX, etc.)
```

---

## Common DNS record types

- **A record** — maps a domain to an IPv4 address
- **AAAA record** — maps a domain to an IPv6 address
- **CNAME** — alias from one domain to another
- **MX** — specifies mail servers for the domain
- **TXT** — arbitrary text, often used for verification and SPF/DKIM email authentication
- **NS** — specifies which nameservers are authoritative for the domain

---

## Why it's fast

Most lookups feel instant because of aggressive caching at every layer — browser, OS, recursive resolver, and ISP. A full lookup from root to authoritative nameserver only happens on cache misses, and even then typically completes in under 100ms.
