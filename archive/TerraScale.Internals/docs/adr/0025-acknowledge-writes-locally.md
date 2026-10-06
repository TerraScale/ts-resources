# Acknowledge public writes locally

A successful public document mutation confirms acceptance by the serving region only. TerraScale does not expose wait-for-replication, region-count, or majority acknowledgement modes. Replication to other selected regions remains asynchronous under the documented convergence and conflict rules.
