from dataclasses import dataclass
from typing import Callable, Optional

@dataclass
class EventBatch:
    n_events: Optional[int] = None
    batch_id: Optional[int] = None
    n_batches: Optional[int] = None
    description: Optional[str] = None

    def __len__(self):
        return self.n_events or 0

    def load(self):
        raise NotImplementedError

    def __str__(self):
        ret = []
        if self.batch_id is not None:
            ret.append(f"{self.__class__.__name__} #{self.batch_id}")
            if self.n_batches is not None:
                ret.append(f"/ {self.n_batches}")
        else:
            ret.append(f"a batch of type {self.__class__.__name__}")

        if self.n_events is not None:
            ret.append(f"containing {self.n_events} events")
        
        if self.description is not None:
            ret.append(f"({self.description})")

        return " ".join(ret)

if __name__ == '__main__':
    print (EventBatch())
    ## Outputs: a batch of type EventBatch

    print (EventBatch(n_events=100))
    ## Outputs: a batch of type EventBatch containing 100 events

    print (EventBatch(n_events=100, description="my super important batch"))
    ## Outputs: a batch of type EventBatch containing 100 events (my super important batch)

    print (EventBatch(n_batches=5, n_events=100))
    ## Outputs: a batch of type EventBatch containing 100 events

    print (EventBatch(batch_id=3, n_events=100, description="Third batch"))
    ## Outputs: EventBatch #3 containing 100 events (Third batch)

    print (EventBatch(batch_id=3, n_events=100, description="Third batch"))
    ## Outputs: EventBatch #3 containing 100 events (Third batch)

    print (EventBatch(batch_id=3, n_batches=5, n_events=100, description="Third batch"))
    ## Outputs: EventBatch #3 / 5 containing 100 events (Third batch)
