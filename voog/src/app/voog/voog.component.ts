import { Component, Input, OnDestroy, OnInit } from '@angular/core';
import { ApiService } from '../api.service';
import { FormControl, FormGroup, ReactiveFormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { Subscription } from 'rxjs';

@Component({
  selector: 'app-voog',
  standalone: true,
  imports: [CommonModule, ReactiveFormsModule],
  templateUrl: './voog.component.html',
  styleUrl: './voog.component.css'
})
export class VoogComponent implements OnInit, OnDestroy {
  voogLearners: any
  buddyLearners: any

  TeacherCodeSubsctiption: Subscription
  TeacherCode = ''

  TimeTableDaySubscription: Subscription
  TimeTableDay = 0

  ngOnInit() {
    this.voogLearners = []
    this.buddyLearners = []

    if (this.TeacherCode != '' && this.TimeTableDay != 0) {
      this.api.getTeacherlessLearnersVoog(this.TeacherCode, this.TimeTableDay).subscribe(data => {
        this.voogLearners = data
        this.api.getTeacherlessLearnersBuddy(this.TeacherCode, this.TimeTableDay).subscribe(data => {
          this.buddyLearners = data
        })
      })
      
    }

  }

  ngOnDestroy() {
    this.TeacherCodeSubsctiption.unsubscribe()  
    this.TimeTableDaySubscription.unsubscribe()
  }

  constructor (private api: ApiService) {
    this.TeacherCodeSubsctiption = api.TeacherCodeSource$.subscribe(
      TeacherCode => {
        this.TeacherCode = TeacherCode
        this.ngOnInit()
      }
    )
    this.TimeTableDaySubscription = api.TimeTableDaySource$.subscribe(
      TimeTableDay => {
        this.TimeTableDay = TimeTableDay
        this.ngOnInit()
      }
    )
  }
}
