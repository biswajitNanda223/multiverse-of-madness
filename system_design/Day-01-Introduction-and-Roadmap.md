# Day 01 — Introduction & Roadmap

> A structured 13-day journey through System Design, from first principles to
> distributed-systems building blocks. This file is the index and mental model
> that ties the rest of the notes together.

---

## 1. What is System Design?

System design is the process of defining the **architecture, components, modules,
interfaces, and data** for a system to satisfy specified requirements. It sits
between *product requirements* and *code*.

Two flavors you will be asked about:

| Type | Focus | Example question |
|------|-------|------------------|
| **High-Level Design (HLD)** | Architecture, services, data flow, trade-offs | "Design Twitter's timeline" |
| **Low-Level Design (LLD)** | Classes, schemas, APIs, design patterns | "Design a parking lot's class model" |

These notes focus mostly on **HLD** with enough LLD to be dangerous.

---

## 2. The mental framework for any design problem

Use this checklist for every problem (interview or real):

1. **Clarify requirements**
   - *Functional*: what the system must do (post tweet, follow user).
   - *Non-functional*: latency, availability, consistency, durability, scale.
2. **Estimate scale** (back-of-envelope): users, QPS, storage, bandwidth.
3. **Define APIs**: the contract between client and server.
4. **Data model**: entities, relationships, access patterns → pick storage.
5. **High-level architecture**: draw the boxes (LB → services → DB → cache).
6. **Deep dive**: the 1–2 hardest components (hot partition, fan-out, etc.).
7. **Identify bottlenecks & scale**: caching, sharding, replication, queues.
8. **Trade-offs & wrap-up**: what you'd improve with more time.

---

## 3. Back-of-the-envelope numbers worth memorizing

**Latency (Jeff Dean's numbers, rounded):**

| Operation | Time |
|-----------|------|
| L1 cache reference | ~1 ns |
| Main memory reference | ~100 ns |
| SSD random read | ~16–150 µs |
| Round trip within datacenter | ~0.5 ms |
| Disk seek (HDD) | ~10 ms |
| Round trip CA ↔ Netherlands | ~150 ms |

**Powers of 2 / data sizes:**

- 1 byte = 8 bits; char = 1 byte; int = 4 bytes.
- KB → MB → GB → TB → PB (×1000 each, roughly).
- 2^10 ≈ 1 thousand, 2^20 ≈ 1 million, 2^30 ≈ 1 billion.

**Time:**

- 1 day ≈ 86,400 s ≈ **~100k seconds**.
- 1 million requests/day ≈ **~12 requests/sec**.

---

## 4. Non-functional requirements (the "-ilities")

- **Scalability** — handle growth (users/data/traffic).
- **Availability** — % uptime (see SLA table in Day 12).
- **Reliability** — performs correctly over time; no data loss.
- **Performance/Latency** — fast response (p50, p95, p99).
- **Consistency** — every read sees the latest write (or not).
- **Durability** — once stored, data survives failures.
- **Maintainability** — easy to operate, debug, evolve.

You almost never get all of them — **system design is the art of trade-offs.**

---

## 5. The 13-day roadmap

| Day | Topic | Theme |
|-----|-------|-------|
| 01 | Introduction & Roadmap | *(this file)* |
| 02 | System Design Basics | Vocabulary, building blocks |
| 03 | Networking Fundamentals | How machines talk |
| 04 | Databases Core | SQL vs NoSQL, ACID, indexing |
| 05 | Caching Basics | Why and how to cache |
| 06 | Architecture Basics | Monolith → microservices, patterns |
| 07 | Load & Scaling | Vertical/horizontal, load balancing |
| 08 | Database Scaling | Sharding, partitioning, federation |
| 09 | Replication & Consistency | CAP, quorums, consistency models |
| 10 | Advanced Caching | Eviction, invalidation, distributed cache |
| 11 | Messaging Systems | Queues, pub/sub, Kafka |
| 12 | Reliability | Availability, fault tolerance, resilience |
| 13 | Storage & CDN | Block/object storage, CDNs |

---

## 6. How to use these notes

- Each day is self-contained but builds on earlier ones.
- Diagrams are described in ASCII/text — sketch them by hand to internalize.
- End-of-file "Key takeaways" = your revision flashcards.

> **Key takeaway:** System design is *requirements → trade-offs → architecture*.
> Master the framework, memorize the numbers, then go deep on building blocks.
