import { Component, Output, EventEmitter, OnDestroy, OnInit } from '@angular/core';
import { RouterLink } from '@angular/router';
import { ApiService } from '../api.service';
import { Subscription } from 'rxjs';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-navigation',
  standalone: true,
  imports: [RouterLink, CommonModule],
  templateUrl: './navigation.component.html',
  styleUrl: './navigation.component.css'
})
export class NavigationComponent implements OnDestroy {
  TeacherCode: string
  TeacherCodeSubsription: Subscription  

  TimeTableDay: number
  TimeTableSubsription: Subscription

  TimeTableDays = [1, 2, 3, 4, 5, 6 ,7, 8]

  voogTeachers: any = []

  onCodeSelect(OnderwyserKode: string) {
    this.api.TeacherCode(OnderwyserKode);
  }

  onDaySelect(Day: string) {
    this.api.TimeTableDay(Number(Day));
  }

  ngOnDestroy() {
    this.TeacherCodeSubsription.unsubscribe()  
    this.TimeTableSubsription.unsubscribe()
  }

  constructor (private api: ApiService) {
    this.api.getVoogTeachers().subscribe(data => {
      this.voogTeachers = data
    })
    this.TeacherCodeSubsription = api.TeacherCodeSource$.subscribe(
      TeacherCode => {
        this.TeacherCode = TeacherCode
      }
    )
    this.TimeTableSubsription = api.TimeTableDaySource$.subscribe(
      TimeTableDay => {
        this.TimeTableDay = TimeTableDay
      }
    )
    this.TeacherCode = ''
    this.TimeTableDay = 1
  }

}

