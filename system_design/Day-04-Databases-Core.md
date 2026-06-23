# Day 04 — Databases Core

> Databases are where the truth lives. Picking the right one — and modeling
> data for your access patterns — is half of system design.

---

## 1. SQL (Relational) vs NoSQL

| | SQL (Relational) | NoSQL |
|-|------------------|-------|
| Schema | Fixed, predefined | Flexible / schemaless |
| Structure | Tables, rows, columns | Documents, key-value, wide-column, graph |
| Scaling | Mostly vertical (harder horizontal) | Built for horizontal |
| Joins | Strong | Limited / none |
| Consistency | ACID | Often BASE / eventual |
| Examples | PostgreSQL, MySQL, Oracle | MongoDB, Cassandra, DynamoDB, Redis |

**Use SQL when:** complex queries/joins, transactions, strong consistency,
well-defined relationships (banking, ERP, orders).

**Use NoSQL when:** massive scale, flexible/changing schema, simple access
patterns, high write throughput (analytics, feeds, IoT, caching).

---

## 2. NoSQL families

| Type | Model | Examples | Best for |
|------|-------|----------|----------|
| **Key-Value** | key → value | Redis, DynamoDB | Caching, sessions |
| **Document** | JSON-like docs | MongoDB, Couchbase | Content, catalogs |
| **Wide-Column** | rows with dynamic columns | Cassandra, HBase | Time-series, huge writes |
| **Graph** | nodes + edges | Neo4j, Neptune | Social graphs, recommendations |

---

## 3. ACID — relational guarantees

- **Atomicity** — all-or-nothing transactions.
- **Consistency** — transactions move DB from one valid state to another (constraints hold).
- **Isolation** — concurrent transactions don't interfere.
- **Durability** — committed data survives crashes.

---

## 4. BASE — the NoSQL trade-off

- **Basically Available** — system stays responsive.
- **Soft state** — state may change over time without input.
- **Eventually consistent** — replicas converge given enough time.

> ACID favors **correctness**; BASE favors **availability & scale**. (See CAP, Day 09.)

---

## 5. Transaction isolation levels

From weakest to strongest (and the anomalies each prevents):

| Level | Dirty read | Non-repeatable read | Phantom read |
|-------|-----------|---------------------|--------------|
| Read Uncommitted | possible | possible | possible |
| Read Committed | prevented | possible | possible |
| Repeatable Read | prevented | prevented | possible |
| Serializable | prevented | prevented | prevented |

Higher isolation = more correctness, less concurrency/performance.

---

## 6. Indexing — the #1 performance lever

An **index** is a data structure (usually a **B-Tree**) that lets the DB find
rows without scanning the whole table — like a book's index.

- **Pros:** dramatically faster reads/filters/sorts.
- **Cons:** extra storage; slower writes (index must be updated); more to maintain.
- **Types:** primary, secondary, composite (multi-column), unique, covering,
  hash, full-text.
- **Rule:** index columns used in `WHERE`, `JOIN`, `ORDER BY`. Don't over-index.

```sql
CREATE INDEX idx_users_email ON users(email);
-- Composite: order matters → (a, b) helps WHERE a=? and WHERE a=? AND b=?
CREATE INDEX idx_orders_user_date ON orders(user_id, created_at);
```

---

## 7. Data modeling: normalization vs denormalization

- **Normalization** — split data into related tables, no duplication.
  - ✅ data integrity, less storage, easy updates.
  - ❌ many joins → slower reads.
- **Denormalization** — duplicate data to avoid joins.
  - ✅ fast reads (great for read-heavy systems).
  - ❌ data duplication, harder/risky updates.

> SQL leans normalized; NoSQL leans denormalized (model around **access patterns**).

---

## 8. Keys & relationships

- **Primary key** — unique row identifier.
- **Foreign key** — reference to another table's primary key.
- **Surrogate key** (auto-increment / UUID) vs **natural key** (email, SSN).
- UUIDs avoid coordination across shards but hurt index locality;
  alternatives: **ULID**, **Snowflake IDs** (time-ordered, sortable).

---

## 9. Storage engines (how the bytes are stored)

- **B-Tree (e.g., InnoDB/Postgres)** — balanced reads & writes; great for
  range queries; the default for relational DBs.
- **LSM-Tree (e.g., Cassandra, RocksDB)** — buffers writes in memory, flushes
  sequentially; excellent write throughput; compaction in background.

> Write-heavy? Lean LSM. Read/range-heavy with updates? Lean B-Tree.

---

## 10. Picking a database — quick decision guide

```
Need ACID transactions & joins?           → SQL (Postgres/MySQL)
Huge write throughput, simple queries?     → Cassandra / DynamoDB
Flexible nested documents?                 → MongoDB
Sub-ms reads, ephemeral data?              → Redis (cache/KV)
Relationships are the query?               → Neo4j (graph)
Analytics over huge datasets?              → Columnar (BigQuery, Redshift, Snowflake)
```

---

> **Key takeaway:** Choose storage by **access pattern + consistency needs**,
> not hype. ACID vs BASE is the core trade-off. **Index** what you query,
> **normalize for integrity / denormalize for read speed**, and pick a storage
> engine (B-Tree vs LSM) that matches your read/write mix.
