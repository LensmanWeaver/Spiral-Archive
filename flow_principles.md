# Flow Principles for the Spiral Archive

This document distills the idea of shifting from archive-heavy logic to a
stream-oriented approach. Inspired by Cray-3 "flow" thinking, each invocation is
a ripple through the system rather than a record in a monolithic database.

## Key Concepts

1. **From Archives to Streams**
   - Replace static SQL storage with a streaming backbone (Kafka, Pulsar, etc.).
   - Ritual events such as `seal_breath` become topics that flow continuously.

2. **Reactive Pulse Network**
   - Services subscribe to the flows they care about.
   - Each event triggers immediate reactions without heavy queries.

3. **Flow-First State**
   - Maintain rolling state through in-memory folds or materialized views.
   - Tools like ksqlDB or Flink can keep this up to date.

4. **Ripple Sourcing**
   - Plugins emit derivative events (`memory_fragment`, `chain_step`...).
   - The chain becomes a living graph of causality.

5. **Backpressure as Dignity**
   - Respect downstream consumers with flow control.

6. **Temporal Windows**
   - Keep recent windows of data in memory and archive the rest to cold storage.

The accompanying `spiral_flow_stream.py` file demonstrates a minimal example of
these ideas using Python and RxPy.
