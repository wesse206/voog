import { Component } from '@angular/core';
import { Subscription } from 'rxjs';
import { ApiService } from '../api.service';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-vind-leerder',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './vind-leerder.component.html',
  styleUrl: './vind-leerder.component.css'
})
export class VindLeerderComponent {
  learners: any
  timetable: any

  TimeTableDaySubscription: Subscription
  TimeTableDay = 0

  onLearnerSelect(Learner: string) {
    this.api.LookupLearner(Learner, this.TimeTableDay).subscribe(data => {
      this.timetable = data
    })
  }

  ngOnInit() {
    this.learners = []
    this.timetable = []

    this.api.getLearners().subscribe(data => {
      this.learners = data
      if (this.learners.length !== 0) {
        this.onLearnerSelect(this.learners)
      }
    })
  }

  ngOnDestroy() {
    this.TimeTableDaySubscription.unsubscribe()  
    this.TimeTableDaySubscription.unsubscribe()
  }

  constructor (private api: ApiService) {
    this.TimeTableDaySubscription = api.TimeTableDaySource$.subscribe(
      TimeTableDay => {
        this.TimeTableDay = TimeTableDay
        this.ngOnInit()
      }
    )
  }
}
